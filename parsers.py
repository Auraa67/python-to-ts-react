import ast
import sys
import util

from pathlib import Path
from typing import NoReturn
from absyn import (
    AnyType, NoneType, IntType, BoolType, Record, Replace, Slice, StrType,
    ListType, Subscript, TupleType, UnionType, FunType, TypeName, ParamType,
    NoneCst, BoolCst, IntCst, StrCst, Var,
    Plus, Times, Minus, And, Or, Not, Cond,
    Is, Equal, Greater, GreaterEq, Less, LessEq,
    Call, Spread, Field, Lambda, List, Tuple,
    IfThenElse, MatchList, MatchData, Return, Raise, TryExcept,
    InitVar, InitVars, TypedVar, FunDef, TypeAlias, DataClass,
    Import, ImportFrom, DeclRegion, CommRegion, ExpRegion,
    ident, typ, exp, comm, decl, prog, block,
)

from error import region
import error

type node_with_region = ast.expr | ast.stmt | ast.type_param | ast.pattern


def get_region(n: node_with_region) -> region:
    return (n.lineno, n.col_offset, n.end_lineno, n.end_col_offset)


def abort(n: node_with_region, err: Exception) -> NoReturn:
    error.fail(get_region(n), err)


def type_to_typ(e: ast.expr) -> typ:
    try:
        match e:
            case ast.Constant(value=None): return NoneType()
            case ast.Name(id='bool'): return BoolType()
            case ast.Name(id='int'): return IntType()
            case ast.Name(id='str'): return StrType()
            case ast.Name(id=n): return TypeName(n)
            case ast.Attribute(ast.Name(id), attr): return TypeName(id + '.' + attr)
            case ast.Subscript(ast.Name(id='Callable'), ast.Tuple([ast.List(ts), rt])):
                return FunType([type_to_typ(t) for t in ts], type_to_typ(rt))
            case ast.Subscript(ast.Name(id='tuple'), ast.Tuple(ts)):
                return TupleType([type_to_typ(t) for t in ts])
            case ast.Subscript(ast.Name(id='Union'), ast.Tuple(ts)):
                return UnionType([type_to_typ(t) for t in ts])
            case ast.Subscript(ast.Name(id='list'), t):
                return ListType(type_to_typ(t))
            case ast.Subscript(ast.Name(id), ast.Tuple(ts)):
                return ParamType(id, [type_to_typ(t) for t in ts])
            case ast.Subscript(ast.Name(id), t):
                return ParamType(id, [type_to_typ(t)])
            case ast.Subscript(ast.Attribute(ast.Name(id), attr), ast.Tuple(ts)):
                return ParamType(id + '.' + attr, [type_to_typ(t) for t in ts])
            case ast.Subscript(ast.Attribute(ast.Name(id), attr), t):
                return ParamType(id + '.' + attr, [type_to_typ(t)])
            case ast.BinOp(left, ast.BitOr(), right):
                return UnionType([type_to_typ(left), type_to_typ(right)])
            case _: raise SyntaxError("unsupported type")
    except SyntaxError as err:
        abort(e, err)


def get_name(e: ast.expr) -> str:
    try:
        match e:
            case ast.Name(id=n): return n
            case _: raise SyntaxError("name expected")
    except SyntaxError as err:
        abort(e, err)


def get_type_name(tp: ast.type_param) -> str:
    try:
        match tp:
            case ast.TypeVar(name=n): return n
            case _: raise SyntaxError("type variable expected")
    except SyntaxError as err:
        abort(tp, err)


def get_field(stm: ast.stmt) -> tuple[str, typ]:
    try:
        match stm:
            case ast.AnnAssign(ast.Name(id), t):
                return (id, type_to_typ(t))
            case _: raise SyntaxError("field declaration expected")
    except SyntaxError as err:
        abort(stm, err)


def get_fields(stms: list[ast.stmt]) -> list[tuple[str, typ]]:
    match stms:
        case [ast.Pass()]:
            return []
        case _:
            return [get_field(stm) for stm in stms]


def get_param(param: ast.arg) -> tuple[ident, typ]:
    if param.annotation is None:
        return (param.arg, AnyType())
    else:
        return (param.arg, type_to_typ(param.annotation))


def stm_to_decl(n: ast.stmt) -> decl:
    d = stm_to_decl_no_region(n)
    if error.regions:
        return DeclRegion(d, get_region(n))
    else:
        return d


def stm_to_decl_no_region(stm: ast.stmt) -> decl:
    try:
        match stm:
            case ast.Import(names=[alias]):
                return Import(alias.name)
            case ast.ImportFrom(module=module, names=aliases) if module is not None:
                return ImportFrom(module, [alias.name for alias in aliases])
            case ast.TypeAlias(name=ast.Name(id), type_params=typ_vars, value=ty):
                typ_var_names = [get_type_name(tv) for tv in typ_vars]
                return TypeAlias(id, typ_var_names, type_to_typ(ty))
            case ast.ClassDef(name=id, type_params=typ_vars, body=stms, decorator_list=dl):
                match dl:
                    case [ast.Name(id="dataclass")]:
                        typ_var_names = [get_type_name(tv) for tv in typ_vars]
                        return DataClass(id, typ_var_names, get_fields(stms))
                    case _:
                        raise SyntaxError("only dataclasses are supported")
            case ast.FunctionDef(name=id, type_params=typ_vars, args=params, returns=ret, body=stms):
                if params.defaults != []: 
                    raise SyntaxError("default values are not supported")
                args = [get_param(arg) for arg in params.args]
                typ_var_names = [get_type_name(tv) for tv in typ_vars]
                if ret is None:
                    return FunDef(id, typ_var_names, args, AnyType(), body_to_block(stms))
                else:
                    return FunDef(id, typ_var_names, args, type_to_typ(ret), body_to_block(stms))
            case ast.Assign([ast.Name(id)], value):
                return InitVar(id, expr_to_exp(value))
            case ast.Assign([ast.Tuple(vars)], value):
                return InitVars([get_name(var) for var in vars], expr_to_exp(value))
            case ast.AnnAssign(ast.Name(id), ty, value) if value is not None:
                return TypedVar(id, type_to_typ(ty), expr_to_exp(value))
            case _: raise SyntaxError("unsupported declaration")
    except SyntaxError as err:
        abort(stm, err)


def get_pattern_name(pat: ast.pattern) -> ident:
    try:
        match pat:
            case ast.MatchAs(name=id):
                return "_" if id is None else id
            case _: raise SyntaxError("identifier expected")
    except SyntaxError as err:
        abort(pat, err)


def get_match_case(mc: ast.match_case) -> tuple[ident, list[tuple[ident, ident]], block]:
    body = body_to_block(mc.body)
    try:
        match mc.pattern:
            case ast.MatchClass(cls=ast.Name(id), kwd_attrs=attrs, kwd_patterns=pats):
                binding = zip(attrs, [get_pattern_name(pat) for pat in pats])
                return (id, list(binding), body)
            case ast.MatchAs(name=id) if id is None:
                return ("_", [], body)
            case _: raise SyntaxError("unsupported dataclass pattern")
    except SyntaxError as err:
        abort(mc.pattern, err)


def get_match_list(mcs: list[ast.match_case]) -> tuple[block, ident, ident, block]:
    match mcs:
        case [ast.match_case(pattern=case1, body=body1), ast.match_case(pattern=case2, body=body2)]:
            orelse = body_to_block(body1)
            ifempty = body_to_block(body2)
            match case1:
                case ast.MatchSequence(patterns=[ast.MatchAs(name=h), ast.MatchStar(name=t)]):
                    hd = "_" if h is None else h
                    tl = "_" if t is None else t
                    match case2:
                        case ast.MatchAs(name=None):
                            return (ifempty, hd, tl, orelse)
                        case _: raise SyntaxError("wildcard required as 'empty list' pattern")
                case _: raise SyntaxError("unsupported 'non-empty list' pattern")
        case _: raise SyntaxError("unsupported list patterns")


def stm_to_comm(n: ast.stmt) -> comm:
    c = stm_to_comm_no_region(n)
    if error.regions:
        return CommRegion(c, get_region(n))
    else:
        return c


def stm_to_comm_no_region(stm: ast.stmt) -> comm:
    try:
        match stm:
            case ast.Match(subject=value, cases=mcs):
                match mcs:
                    case [ast.match_case(pattern=ast.MatchClass()), *_]:
                        return MatchData(expr_to_exp(value), [get_match_case(mc) for mc in mcs])
                    case [ast.match_case(pattern=ast.MatchSequence()), *_]:
                        (ifempty, hd, tl, notempty) = get_match_list(mcs)
                        return MatchList(expr_to_exp(value), ifempty, hd, tl, notempty)
                    case _: raise SyntaxError("Unsupported dataclass patterns")
            case ast.If(test=cmp, body=body, orelse=orelse):
                return IfThenElse(expr_to_exp(cmp), body_to_block(body), body_to_block(orelse))
            case ast.Try(body=body, handlers=handlers):
                match handlers:
                    case [ast.ExceptHandler(type=ast.Name(id=exn), name=name, body=handler)]:
                        if name is None:
                            raise SyntaxError("exception name required in except clause")
                        else:
                            return TryExcept(body_to_block(body), exn, name, body_to_block(handler))
                    case _: raise SyntaxError("multiple handlers not supported")
            case ast.Return(value=value) if value is not None:
                return Return(expr_to_exp(value))
            case ast.Raise(exc=ast.Name(id=id)):
                return Raise(id, [])
            case ast.Raise(exc=ast.Call(func=ast.Name(id), args=args)):
                return Raise(id, [expr_to_exp(arg) for arg in args])
            case _: raise SyntaxError("unsupported statement")
    except SyntaxError as err:
        abort(stm, err)


def expr_to_exp(n: ast.expr) -> exp:
    e = expr_to_exp_no_region(n)
    if error.regions:
        return ExpRegion(e, get_region(n))
    else:
        return e


def expr_to_exp_no_region(e: ast.expr) -> exp:
    try:
        match e:
            case ast.Name(id):
                return Var(id)
            case ast.Constant(value=None):
                return NoneCst()
            case ast.Constant(b) if type(b) is bool:
                return BoolCst(b)
            case ast.Constant(i) if type(i) is int:
                return IntCst(i)
            case ast.Constant(s) if type(s) is str:
                return StrCst(s)
            case ast.UnaryOp(ast.USub(), ast.Constant(value=i)) if type(i) is int:
                return IntCst(-i)
            case ast.BinOp(left, ast.Add(), right):
                e1 = expr_to_exp(left)
                e2 = expr_to_exp(right)
                return Plus(e1, e2)
            case ast.BinOp(left, ast.Sub(), right):
                e1 = expr_to_exp(left)
                e2 = expr_to_exp(right)
                return Minus(e1, e2)
            case ast.BinOp(left, ast.Mult(), right):
                e1 = expr_to_exp(left)
                e2 = expr_to_exp(right)
                return Times(e1, e2)
            case ast.Compare(left, [ast.Is()], [right]):
                e1 = expr_to_exp(left)
                e2 = expr_to_exp(right)
                return Is(e1, e2)
            case ast.Compare(left, [ast.Eq()], [right]):
                e1 = expr_to_exp(left)
                e2 = expr_to_exp(right)
                return Equal(e1, e2)
            case ast.Compare(left, [ast.Lt()], [right]):
                e1 = expr_to_exp(left)
                e2 = expr_to_exp(right)
                return Less(e1, e2)
            case ast.Compare(left, [ast.Gt()], [right]):
                e1 = expr_to_exp(left)
                e2 = expr_to_exp(right)
                return Greater(e1, e2)
            case ast.Compare(left, [ast.LtE()], [right]):
                e1 = expr_to_exp(left)
                e2 = expr_to_exp(right)
                return LessEq(e1, e2)
            case ast.Compare(left, [ast.GtE()], [right]):
                e1 = expr_to_exp(left)
                e2 = expr_to_exp(right)
                return GreaterEq(e1, e2)
            case ast.BoolOp(ast.And(), [left, right]):
                e1 = expr_to_exp(left)
                e2 = expr_to_exp(right)
                return And(e1, e2)
            case ast.BoolOp(ast.Or(), [left, right]):
                e1 = expr_to_exp(left)
                e2 = expr_to_exp(right)
                return Or(e1, e2)
            case ast.UnaryOp(ast.Not(), operand):
                e1 = expr_to_exp(operand)
                return Not(e1)
            case ast.IfExp(test=cmp, body=value, orelse=orelse):
                return Cond(expr_to_exp(value), expr_to_exp(cmp), expr_to_exp(orelse))
            case ast.Starred(operand):
                e1 = expr_to_exp(operand)
                return Spread(e1)
            case ast.Subscript(value, ast.Slice(lower, upper)) if lower is not None:
                return Slice(expr_to_exp(value), expr_to_exp(lower), None if upper is None else expr_to_exp(upper))
            case ast.Subscript(value, index):
                return Subscript(expr_to_exp(value), expr_to_exp(index)) 
            case ast.Tuple(elts):
                return Tuple([expr_to_exp(elt) for elt in elts])
            case ast.List(elts):
                return List([expr_to_exp(elt) for elt in elts])
            case ast.Call(ast.Name("replace"), [value], kwargs):
                fields = [(kwarg.arg, expr_to_exp(kwarg.value)) for kwarg in kwargs if kwarg.arg is not None]
                return Replace(expr_to_exp(value), fields)
            case ast.Call(ast.Name(id), args, []):
                if str.isupper(id[0]):
                    if args == []:
                        return Record(id, [])
                    else:
                        raise SyntaxError("unsupported expression, keywords are required")
                else:
                    return Call(id, [expr_to_exp(arg) for arg in args])
            case ast.Call(ast.Name(id), [], kwargs):
                if str.isupper(id[0]):
                    if any(kwarg.arg is None for kwarg in kwargs):
                        raise SyntaxError("unsupported expression, missing keyword")
                    fields = [(kwarg.arg, expr_to_exp(kwarg.value)) for kwarg in kwargs if kwarg.arg is not None]
                    return Record(id, fields)
                else:
                    raise SyntaxError("unsupported expression, keywords not allowed")
            case ast.Call(ast.Attribute(ast.Name(module), func), args):
                return Call(module + "." + func, [expr_to_exp(arg) for arg in args])
            case ast.Attribute(ast.Name(id), attr):
                return Field(id, attr)
            case ast.Lambda(params, body):
                ids: list[str] = [param.arg for param in params.args]
                return Lambda(ids, expr_to_exp(body))
            case _: raise SyntaxError("unsupported expression")
    except SyntaxError as err:
        abort(e, err)


def body_to_block(body: list[ast.stmt]) -> block:
    match body:
        case [*stms, stm]:
            ds = [stm_to_decl(s) for s in stms]
            c = stm_to_comm(stm)
            return (ds, c)
        case _:
            raise SyntaxError("unexpected empty body")


def stmts_to_prog(body: list[ast.stmt]) -> prog:
    match body:
        case [*stms, ast.Expr(value)]:
            error.module = False
            ds = [stm_to_decl(s) for s in stms]
            e = expr_to_exp(value)
            return (ds, e)
        case _:
            error.module = True
            return ([stm_to_decl(s) for s in body], None)


def mod_to_prog(m: ast.mod) -> prog:
    match m:
        case ast.Module(body):
            return stmts_to_prog(body)
        case _:
            raise SyntaxError("module required")


def extract_region(err: SyntaxError) -> region:
    # 'offset' and 'end_offset' are 1-indexed
    if err.lineno is None:
        return (1, 0, None, None)
    elif err.offset is None or err.offset == 0:
        return (err.lineno, 0, None, None)
    elif err.end_lineno is None or err.end_lineno == 0:
        return (err.lineno, err.offset - 1, None, None)
    elif err.end_offset is None or err.end_offset == 0:
        return (err.lineno, err.offset - 1, err.end_lineno + 1, 0)
    else:
        return (err.lineno, err.offset - 1, err.end_lineno, err.end_offset - 1)


def parse_from_str(src: str) -> prog:
    try:
        t: ast.Module = ast.parse(src, error.filename)
        # print(ast.dump(t, indent=2))
        # print(ast.unparse(t))
        result = mod_to_prog(t)
        # print(result)
        return result
    except SyntaxError as err:
        # print(err.lineno, err.offset, err.end_lineno, err.end_offset)
        error.fail(extract_region(err), SyntaxError(err.msg))


def parse_from_file(filename: str) -> prog:
    try:
        error.filename = filename
        src = Path(filename).read_text()
        return parse_from_str(src)
    except FileNotFoundError as err:
        sys.exit(str(err))


def parse_with_regions(filename: str) -> prog:
    error.regions = True
    return parse_from_file(filename)


def main() -> None:
    p = parse_from_file("examples/misc.py")
    #print(p)
    print(util.display(p))


if __name__ == '__main__':
    main()

import error
import parsers


from absyn import (
    AnyType, Import, ImportFrom, NoneType, IntType, BoolType, StrType,
    ListType, Subscript, TupleType, UnionType, FunType, TypeName, ParamType,
    NoneCst, BoolCst, IntCst, StrCst, Var, Plus, Times, Minus,
    Is, Equal, Greater, GreaterEq, Less, LessEq, And, Or, Not, Cond,
    Call, Spread, Field, Lambda, List, Tuple, Record, Replace, Slice, 
    IfThenElse, MatchList, MatchData, Return, Raise, TryExcept,
    InitVar, InitVars, TypedVar, FunDef, TypeAlias, DataClass,
    ExpRegion, CommRegion, DeclRegion,
    ident, typ, exp, comm, decl, prog, block,
)


def str_of_typ(t: typ) -> str:
    match t:
        case AnyType():
            return "Any"
        case NoneType():
            return "None"
        case IntType():
            return "int"
        case BoolType():
            return "bool"
        case StrType():
            return "str"
        case ListType(ty=ty):
            return "list[" + str_of_typ(ty) + "]"
        case TupleType(tys=tys):
            return "tuple[" + ", ".join(map(str_of_typ, tys)) + "]"
        case UnionType(tys=tys):
            return " | ".join(map(str_of_typ, tys))
        case FunType(argtypes=arg, returns=ret):
            return "Callable[[" + ", ".join(map(str_of_typ, arg)) + "], " + str_of_typ(ret) + "]"
        case ParamType(id=id, tys=tys):
            return id + "[" + ", ".join(map(str_of_typ, tys)) + "]"
        case TypeName(id=id):
            return id
        case _:
            raise NotImplementedError


def str_of_exp(e: exp, paren: bool = True) -> str:
    def par(s: str) -> str:
        return "(" + s + ")" if paren else s
    match e:
        case Var(id=id):
            return id
        case NoneCst():
            return "None"
        case BoolCst(value=b):
            return str(b)
        case IntCst(value=q):
            return str(q)
        case StrCst(value=s):
            return '"' + s + '"'
        case Plus(left=e1, right=e2):
            return par(str_of_exp(e1) + " + " + str_of_exp(e2))
        case Times(left=e1, right=e2):
            return par(str_of_exp(e1) + " * " + str_of_exp(e2))
        case Minus(left=e1, right=e2):
            return par(str_of_exp(e1) + " - " + str_of_exp(e2))
        case Is(left=e1, right=e2):
            return par(str_of_exp(e1) + " is " + str_of_exp(e2))
        case Equal(left=e1, right=e2):
            return par(str_of_exp(e1) + " == " + str_of_exp(e2))
        case Less(left=e1, right=e2):
            return par(str_of_exp(e1) + " < " + str_of_exp(e2))
        case LessEq(left=e1, right=e2):
            return par(str_of_exp(e1) + " <= " + str_of_exp(e2))
        case Greater(left=e1, right=e2):
            return par(str_of_exp(e1) + " > " + str_of_exp(e2))
        case GreaterEq(left=e1, right=e2):
            return par(str_of_exp(e1) + " >= " + str_of_exp(e2))
        case And(left=e1, right=e2):
            return par(str_of_exp(e1) + " and " + str_of_exp(e2))
        case Or(left=e1, right=e2):
            return par(str_of_exp(e1) + " or " + str_of_exp(e2))
        case Not(operand=exp):
            return par("not" + str_of_exp(exp))
        case Cond(value=value, test=test, orelse=orelse):
            return par(str_of_exp(value) + " if " + str_of_exp(test) + " else " + str_of_exp(orelse))
        case Call(func=ident, args=args):
            return par(ident+ "(" + ", ".join(map(lambda x:str_of_exp(x, paren=False), args)) + ")")
        case Lambda(args=args, body=body):
            return par("lambda " + ", ".join(args) + ": " + str_of_exp(body, paren=False))
        case Tuple(exps=exps):
            return "(" + ", ".join(map(lambda x: str_of_exp(x, paren=False), exps)) + ")"
        case List(exps=exps):
            return "[" + ", ".join(map(lambda x: str_of_exp(x, paren=False), exps)) + "]"
        case Subscript(value=value, index=index):
            return str_of_exp(value) + "[" + str_of_exp(index, paren=False) + "]"
        case Slice(value=value, lower=lower, upper=upper):
            if upper is None:
                return str_of_exp(value) + "[" + str_of_exp(lower, paren=False) + ":" + "]"
            else:
                return str_of_exp(value) + "[" + str_of_exp(lower, paren=False) + ":" + str_of_exp(upper, paren=False) + "]"
        case Spread(operand=operand):
            return "*" + str_of_exp(operand)
        case Record(id=id, kwargs=kwargs):
            return par(id + "(" + ", ".join(map(lambda x: x[0] + "=" + str_of_exp(x[1], paren=False), kwargs)) + ")")
        case Field(id=id, attr=attr):
            return id + "." + attr
        case Replace(value=value, kwargs=kwargs):
            return par("replace(" + str_of_exp(value, paren=False) + ", " + ", ".join(map(lambda x: x[0] + "=" + str_of_exp(x[1], paren=False), kwargs)) + ")")
        case ExpRegion(contents=e1, reg=r):
            try:
                return str_of_exp(e1, paren)
            except Exception as err:
                return error.fail(r, err)
        case _:
            raise NotImplementedError


def newline(depth: int = 0, indent: str ="    ") -> str:
    return "\n" + depth * indent


def str_of_comm(depth: int, c: comm) -> str:
    match c:
        case IfThenElse(test=test, body=body, orelse=orelse):
            return (newline(depth) + "if " + str_of_exp(test, paren=False) + ":" +
                    str_of_block(depth + 1, body) +
                    newline(depth) + "else:" +
                    str_of_block(depth + 1, orelse))
        case MatchList(subject=subject, ifempty=ifempty, hd=hd, tl=tl, orelse=orelse):
            return (
                    newline(depth) + "match " + str_of_exp(subject, paren=False) + ":" +
                    newline(depth + 1) + "case [" + hd + ", *" + tl + "]:" +
                    str_of_block(depth + 2, orelse) +
                    newline(depth + 1) + "case _:" +
                    str_of_block(depth + 2, ifempty)
            )
        case MatchData(subject=subject, cases=cases):
            return (
                    newline(depth) + "match " + str_of_exp(subject, paren=False) + ":" +
                    "".join(map(lambda c: 
                    (newline(depth + 1) + "case _:" + str_of_block(depth + 2, c[2]))
                    if c[0] == "_" else 
                    (newline(depth + 1) + "case " + c[0] + "(" +
                    ", ".join(map(lambda b: b[0] + "=" + b[1], c[1])) + "):" + 
                    str_of_block(depth + 2, c[2])), cases))
            )
        case Return(value=value):
            return (
                    newline(depth) + "return " +
                    str_of_exp(value, paren=False)
            )
        case Raise(exn=exn, exps=exps):
            if exps:
                return (newline(depth) + "raise " + exn + "(" + 
                ", ".join(map(lambda x: str_of_exp(x, paren=False), exps)) + ")")
            else:
                return newline(depth) + "raise " + exn
        case TryExcept(body=body, exn=exn, name=name, handler=handler):
            return (
                    newline(depth) + "try:" +
                    str_of_block(depth + 1, body) + 
                    newline(depth) + "except " + exn + " as " + name + ":" +
                    str_of_block(depth + 1, handler)
            )
        case CommRegion(contents=e1, reg=r):
            try:
                return str_of_comm(depth, e1)
            except Exception as err:
                return error.fail(r, err)
        case _:
            raise NotImplementedError


def str_of_block(depth: int, b: block) -> str:
    match b:
        case(ds, c):
            return str_of_decls(ds, depth) + str_of_comm(depth, c)

def str_of_decl(depth: int, d: decl) -> str:
    match d:
        case InitVar(id=id, value=value):
            return (newline(depth) + id + " = " + str_of_exp(value, paren=False))
        case TypedVar(id=id, ty=ty, value=value):
            return (newline(depth) + id + ": " + str_of_typ(ty) + " = " + str_of_exp(value, paren=False))
        case Import(module=module):
            return newline(depth) + "import " + module
        case ImportFrom(module=module, names=names):
            return newline(depth) + "from " + module + " import " + ", ".join(names)
        case InitVars(ids=ids, value=value):
            return newline(depth) + "(" + ", ".join(ids) + ") = " + str_of_exp(value, paren=False)
        case FunDef(id=id, tps=tps, args=args, ret=ret, body=body):
            if tps == []:
                return newline(depth) + "def " + id + "(" + ", ".join(map(lambda x: x[0] + ": " + str_of_typ(x[1]), args)) + ") -> " + str_of_typ(ret) + ":" + str_of_block(depth + 1, body)
            else:
                return newline(depth) + "def " + id + "[" + ", ".join(tps) + "]" + "(" + ", ".join(map(lambda x: x[0] + ": " + str_of_typ(x[1]), args)) + ") -> " + str_of_typ(ret) + ":" + str_of_block(depth + 1, body)
        case DataClass(id=id, tps=tps, fields=fields):
            checking_fields = newline(depth + 1).join(map(lambda x: x[0] + ": " + str_of_typ(x[1]), fields)) if fields else "pass"
            if tps == []:
                return newline(depth) + "@dataclass" + newline(depth) + "class " + id + ":" + newline(depth + 1) + checking_fields
            else:
                return newline(depth) + "@dataclass" + newline(depth) + "class " + id + "[" + ", ".join(tps) + "]:" + newline(depth + 1) + checking_fields
        case TypeAlias(id=id, tps=tps, ty=ty):
            check_tps = "[" + ", ".join(tps)  + "]" if tps else ""
            return newline(depth) + "type " + id + check_tps + " = " + str_of_typ(ty)
        case DeclRegion(contents=d1, reg=r):
            try:
                return str_of_decl(depth, d1)
            except Exception as err:
                return error.fail(r, err)
        case _:
            raise NotImplementedError



def str_of_decls(ds: list[decl], depth: int = 0) -> str:
    return "".join([str_of_decl(depth, d) for d in ds])


def str_of_prog(p: prog) -> str:
    (ds, e) = p
    str_of_ds = str_of_decls(ds).strip()
    if e is None:
        return str_of_ds
    else:
        return str_of_ds + "\n\n" + str_of_exp(e, paren=False)



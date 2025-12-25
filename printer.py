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
    ident, typ, exp, binding, comm, decl, prog, block,
)


std_types = {
    "TextIOWrapper": "FileReader",
}

std_exns = {
    "SystemExit": "Error",
    "ValueError": "Error",
    "IndexError": "RangeError",
    "Exception": "Error",
}

# Some int value indicates the object argument for the method
# None if the target is a function
primitives: dict[str, tuple[str, int | None]] = {
    "print": ("console.log", None),
    "str": ("toString", 0),
#   "map": ("map", 1),
#   "filter": ("filter", 1),
    "functools.reduce": ("reduce", 0),
}

ignored_imports = ["typing", "dataclasses", "collections.abc"]


def str_of_typ(t: typ) -> str:
    match t:
        case AnyType():
            return "any"
        case NoneType():
            return "undefined"
        case IntType():
            return "number"
        case BoolType():
            return "boolean"
        case StrType():
            return "string"
        case ListType(ty=ty):
            return str_of_typ(ty) + "[]"
        case TupleType(tys=tys):
            return  "[" + ", ".join(map(str_of_typ, tys)) + "]"
        case UnionType(tys=tys):
            return " | ".join(map(str_of_typ, tys))
        case FunType(argtypes=argtypes, returns=returns):
            args_string = map(
                lambda i: f"arg{i}: {str_of_typ(argtypes[i])}",
                range(len(argtypes))
            )
            return "(" + ", ".join(args_string) + ") => " + str_of_typ(returns)
        case ParamType(id=id, tys=tys):
            return id + "<" + ", ".join(map(str_of_typ, tys)) + ">"
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
            return "undefined"
        case BoolCst(value=b):
            return "true" if b else "false"
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
            return par(str_of_exp(e1) + " === " + str_of_exp(e2))
        case Equal(left=e1, right=e2):
            return par(str_of_exp(e1) + " == " + str_of_exp(e2))
        case Less(left=left, right=right):
            return par(str_of_exp(left) + " < " + str_of_exp(right))
        case LessEq(left=left, right=right):
            return par(str_of_exp(left) + " <= " + str_of_exp(right))
        case Greater(left=left, right=right):
            return par(str_of_exp(left) + " > " + str_of_exp(right))
        case GreaterEq(left=left, right=right):
            return par(str_of_exp(left) + " >= " + str_of_exp(right))
        case And(left=left, right=right):
            return par(str_of_exp(left) + " && " + str_of_exp(right))
        case Or(left=left, right=right):
            return par(str_of_exp(left) + " || " + str_of_exp(right))
        case Not(operand=operand):
            return par("!" + str_of_exp(operand))
        case Cond(value=value, test=test, orelse=orelse):
            return par(str_of_exp(test) + " ? " + str_of_exp(value) + " : " + str_of_exp(orelse))
        case Call(func=func, args=args):
            return func + "(" + ", ".join(map(lambda arg: str_of_exp(arg), args)) + ")"
        case Lambda(args=args, body=body):
            return par("(" + ", ".join(args) + ") => " + str_of_exp(body))
        case Tuple(exps=exps):
            return "[" + ", ".join(map(str_of_exp, exps)) + "]"
        case List(exps=exps):
            return "[" + ", ".join(map(str_of_exp, exps)) + "]"
        case Subscript(value=value, index=index):
            return str_of_exp(value) + "[" + str_of_exp(index) + "]"
        case Slice(value=value, lower=lower, upper=upper):
            args = [str_of_exp(lower)]
            if upper is not None:
                args.append(str_of_exp(upper))
            return str_of_exp(value) + ".slice(" + ", ".join(args) + ")"
        case Spread(operand=operand):
            return "..." + str_of_exp(operand)
        case Record(fields=fields):
            return "{" + ", ".join(map(lambda kv: kv[0] + ": " + str_of_exp(kv[1]), fields)) + "}"
        case Field(value=value, field=field):
            return str_of_exp(value) + "." + field
        case Replace(value=value, kwargs=kwargs):
            return "{" + "..."+ str_of_exp(value) + ", " + ", ".join(map(lambda kv: kv[0] + ": " + str_of_exp(kv[1]), kwargs)) + "}"
        case ExpRegion(contents=e1, reg=r):
            try:
                return str_of_exp(e1, paren)
            except Exception as err:
                error.fail(r, err)
        case _:
            raise NotImplementedError()


def newline(depth: int = 0, indent: str = "    ") -> str:
    return "\n" + depth * indent


def str_of_comm(depth: int, c: comm) -> str:
    match c:
        case IfThenElse(test=test, body=body, orelse=orelse):
            return (newline(depth) + "if (" + str_of_exp(test, paren=False) + ") {" +
                    str_of_block(depth + 1, body) +
                    newline(depth) + "} else {" +
                    str_of_block(depth + 1, orelse) +
                    newline(depth) + "}")
        case MatchList(subject=subject, ifempty=ifempty, hd=hd, tl=tl, orelse=orelse):
            return (
                newline(depth) + "if (" + str_of_exp(subject)+ ".length === 0) {" +
                str_of_block(depth + 1, ifempty) + newline(depth) + "} else {" + newline(depth + 1) +
                "const " + hd + "= " + str_of_exp(subject) + "[0];" + newline(depth + 1) +
                "const " + tl + "= " + str_of_exp(subject) + ".slice(1);" +
                str_of_block(depth + 1, orelse) + newline(depth) + "}"
            )
        case MatchData(subject=subject, cases=cases):
            subject_str = str_of_exp(subject)
            return (
                newline(depth) + " else ".join(map(lambda x: "if (" + subject_str + ".kind === \"" + x[0] + "\") {" +
                newline(depth + 1) + "const " + ", ".join(map(lambda y: f"{y[0]}: {y[1]}", x[1])) + " = " + subject_str + ".value;" +
                newline(depth + 1) + str_of_block(depth + 1, x[2]) + newline(depth) + "}", cases))
            )
        case Return(value=value):
            return newline(depth) + "return " + str_of_exp(value) + ";"
        case Raise(exn=exn, exps=exps):
            return newline(depth) + "throw new " + exn + f"({", ".join(map(str_of_exp, exps))});"
        case TryExcept(body=body, exn=exn, name=name, handler=handler):
            return (
                newline(depth) + "try {" + str_of_block(depth + 1, body) +
                newline(depth) + "} catch (" + name + ") {" +
                newline(depth + 1) + "if (" + name + " instanceof " + exn + ") {" +
                str_of_block(depth + 2, handler) +
                newline(depth + 1) + "} else {" + 
                newline(depth + 2) + "throw " + name + ";" +
                newline(depth + 1) + "}" +
                newline(depth) + "}"
            )
        case CommRegion(contents=e1, reg=r):
            try:
                return str_of_comm(depth, e1)
            except Exception as err:
                error.fail(r, err)
        case _:
            raise NotImplementedError()


def str_of_block(depth: int, b: block) -> str:
    decls, command = b
    s_decls = "".join(map(lambda d: str_of_decl(depth, d), decls))
    s_comm = str_of_comm(depth, command)
    return s_decls + s_comm

def str_of_decl(depth: int, d: decl) -> str:
    match d:
        case InitVar(id=id, value=value):
            return (newline(depth) + "const " + id + " = " + str_of_exp(value, paren=False))
        case TypedVar(id=id, ty=ty, value=value):
            return (newline(depth) + "const " + id + ": " + str_of_typ(ty) + " = " + str_of_exp(value, paren=False))
        case Import(module=module):
            return (newline(depth) + "import * as " + module + " from \"./" + module + "\";")
        case ImportFrom(module=module, names=names):
            return (newline(depth) + "import { " + ", ".join(names) + " } from \"./" + module + "\";")
        case InitVars(ids=ids, value=value):
            return  (newline(depth) + "let " + ", ".join(map(lambda x: x + "=" + str_of_exp(value), ids)) + ";")
        case FunDef(id=id, tps=tps, args=args, ret=ret, body=body):
            lists = "<" + ", ".join(tps) + ">" if tps else ""
            arguments = ", ".join(map(lambda x: x[0] + ": " + str_of_typ(x[1]), args))
            return (newline(depth) + "function " + id + lists + "(" + arguments + "): " + str_of_typ(ret) + " {" + str_of_block(depth + 1, body) + newline(depth) + "}")
        # TODO Add missing cases
        case DeclRegion(contents=d1, reg=r):
            try:
                return str_of_decl(depth, d1)
            except Exception as err:
                error.fail(r, err)
        case _:
            raise NotImplementedError()


def str_of_decls(ds: list[decl], depth: int = 0) -> str:
    return "".join([str_of_decl(depth, d) for d in ds])


def str_of_prog(p: prog) -> str:
    (ds, e) = p
    str_of_ds = str_of_decls(ds).strip()
    if e is None:
        return str_of_ds
    else:
        return str_of_ds + "\n\n" + str_of_exp(e, paren=False)


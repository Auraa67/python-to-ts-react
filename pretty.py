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
        # TODO Add missing cases
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
        # TODO Add missing cases
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
        # TODO Add missing cases
        case CommRegion(contents=e1, reg=r):
            try:
                return str_of_comm(depth, e1)
            except Exception as err:
                return error.fail(r, err)
        case _:
            raise NotImplementedError


def str_of_block(depth: int, b: block) -> str:
    raise NotImplementedError # TODO Replace this line with your code


def str_of_decl(depth: int, d: decl) -> str:
    match d:
        case InitVar(id=id, value=value):
            return (newline(depth) + id + " = " + str_of_exp(value, paren=False))
        case TypedVar(id=id, ty=ty, value=value):
            return (newline(depth) + id + ": " + str_of_typ(ty) + " = " + str_of_exp(value, paren=False))
        # TODO Add missing cases
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



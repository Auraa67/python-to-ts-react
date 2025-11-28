from typing import Union
from dataclasses import dataclass
from error import region


type ident = str


type typ = Union[
    AnyType,  # ...
    NoneType,  # ...
    IntType,  # ...
    BoolType,  # ...
    StrType,  # ...
    ListType,  # ty: typ
    TupleType,  # tys: list[typ]
    UnionType,  # tys: list[typ]
    FunType,  # argtypes: list[typ]; returns: typ
    ParamType,  # id: ident; tys: list[typ]
    TypeName,  # id: ident
]


type exp = Union[
    NoneCst,  # ...
    IntCst,  # value: int
    StrCst,  # value: str
    BoolCst,  # value: bool
    Var,  # id: ident
    Plus,  # left: exp; right: exp
    Times,  # left: exp; right: exp
    Minus,  # left: exp; right: exp
    Is,  # left: exp; right: exp
    Equal,  # left: exp; right: exp
    Less,  # left: exp; right: exp
    LessEq,  # left: exp; right: exp
    Greater,  # left: exp; right: exp
    GreaterEq,  # left: exp; right: exp
    And,  # left: exp; right: exp
    Or,  # left: exp; right: exp
    Not,  # operand: exp
    Cond,  # value: exp; test: exp; orelse: exp
    Call,  # func: ident; args: list[exp]
    Lambda,  # args: list[ident]; body: exp
    Tuple,  # exps: list[exp]
    List,  # exps: list[exp]
    Subscript,  # value: exp; index: exp
    Slice,  # value: exp; lower: exp; upper: exp | None
    Spread,  # operand: exp
    Record,  # id: ident; kwargs: list[tuple[ident, exp]]
    Field,  # id: ident; attr: ident
    Replace,  # value: exp; kwargs: list[tuple[ident, exp]]
    ExpRegion,  # contents: exp; reg: region
]


type binding = list[tuple[ident, ident]]


type comm = Union[
    IfThenElse,  # test: exp; body: block; orelse: block
    MatchList,  # subject: exp; ifempty: block; hd: ident; tl: ident; orelse: block
    MatchData,  # subject: exp; cases: list[tuple[ident, binding, block]]
    Return,  # value: exp
    Raise,  # exn: ident; exps: list[exp]
    TryExcept,  # body: block; exn: ident; name: ident; handler: block
    CommRegion,  # contents: comm; reg: region
]


type block = tuple[list[decl], comm]


type decl = Union[
    Import,  # module: ident
    ImportFrom,  # module: ident; names: list[ident]
    InitVar,  # id: ident; value: exp
    InitVars,  # ids: list[ident]; value: exp
    TypedVar,  # id: ident; ty: typ; value: exp
    FunDef,  # id: ident; tps: list[ident]; args: list[tuple[ident, typ]]; ret: typ; body: block
    DataClass,  # id: ident; tps: list[ident]; fields: list[tuple[ident, typ]]
    TypeAlias,  # id: ident; tps: list[ident]; ty: typ
    DeclRegion,  # contents: decl; reg: region
]


type prog = tuple[list[decl], exp | None]

# dataclasses


# type typ


@dataclass
class AnyType: ...


@dataclass
class NoneType: ...


@dataclass
class IntType: ...


@dataclass
class BoolType: ...


@dataclass
class StrType: ...


@dataclass
class ListType: ty: typ


@dataclass
class TupleType: tys: list[typ]


@dataclass
class UnionType: tys: list[typ]


@dataclass
class FunType: argtypes: list[typ]; returns: typ


@dataclass
class ParamType: id: ident; tys: list[typ]


@dataclass
class TypeName: id: ident


# type exp


@dataclass
class NoneCst: ...


@dataclass
class IntCst: value: int


@dataclass
class StrCst: value: str


@dataclass
class BoolCst: value: bool


@dataclass
class Var: id: ident


@dataclass
class Plus: left: exp; right: exp


@dataclass
class Times: left: exp; right: exp


@dataclass
class Minus: left: exp; right: exp


@dataclass
class Is: left: exp; right: exp


@dataclass
class Equal: left: exp; right: exp


@dataclass
class Less: left: exp; right: exp


@dataclass
class LessEq: left: exp; right: exp


@dataclass
class Greater: left: exp; right: exp


@dataclass
class GreaterEq: left: exp; right: exp


@dataclass
class And: left: exp; right: exp


@dataclass
class Or: left: exp; right: exp


@dataclass
class Not: operand: exp


@dataclass
class Cond: value: exp; test: exp; orelse: exp


@dataclass
class Call: func: ident; args: list[exp]


@dataclass
class Lambda: args: list[ident]; body: exp


@dataclass
class Tuple: exps: list[exp]


@dataclass
class List: exps: list[exp]


@dataclass
class Subscript: value: exp; index: exp


@dataclass
class Slice: value: exp; lower: exp; upper: exp | None


@dataclass
class Spread: operand: exp


@dataclass
class Record: id: ident; kwargs: list[tuple[ident, exp]]


@dataclass
class Field: id: ident; attr: ident


@dataclass
class Replace: value: exp; kwargs: list[tuple[ident, exp]]


@dataclass
class ExpRegion: contents: exp; reg: region


# type comm


@dataclass
class IfThenElse: test: exp; body: block; orelse: block


@dataclass
class MatchList: subject: exp; ifempty: block; hd: ident; tl: ident; orelse: block


@dataclass
class MatchData: subject: exp; cases: list[tuple[ident, binding, block]]


@dataclass
class Return: value: exp


@dataclass
class Raise: exn: ident; exps: list[exp]


@dataclass
class TryExcept: body: block; exn: ident; name: ident; handler: block


@dataclass
class CommRegion: contents: comm; reg: region


# type decl


@dataclass
class Import: module: ident


@dataclass
class ImportFrom: module: ident; names: list[ident]


@dataclass
class InitVar: id: ident; value: exp


@dataclass
class InitVars: ids: list[ident]; value: exp


@dataclass
class TypedVar: id: ident; ty: typ; value: exp


@dataclass
class FunDef: id: ident; tps: list[ident]; args: list[tuple[ident, typ]]; ret: typ; body: block


@dataclass
class DataClass: id: ident; tps: list[ident]; fields: list[tuple[ident, typ]]


@dataclass
class TypeAlias: id: ident; tps: list[ident]; ty: typ


@dataclass
class DeclRegion: contents: decl; reg: region

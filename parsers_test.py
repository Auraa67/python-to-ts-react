# import pytest
import parsers
import util

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

# pyright: reportAttributeAccessIssue=false

src = ""
ast = ([], None)

def test_parse_from_str_empty() -> None:
    assert ast == parsers.parse_from_str(src)


src000 = "None"
ast000 = ([], NoneCst())

def test_parse_from_str000() -> None:
    assert ast000 == parsers.parse_from_str(src000)


src001 = "True"
ast001 = ([], BoolCst(value=True))

def test_parse_from_str001() -> None:
    assert ast001 == parsers.parse_from_str(src001)


src100 = "x = 42"
ast100 = ([InitVar(id='x', value=IntCst(value=42))], None)

def test_parse_from_str100() -> None:
    assert ast100 == parsers.parse_from_str(src100)


src101 = "b = False"
ast101 = ([InitVar(id='b', value=BoolCst(value=False))], None)

def test_parse_from_str101() -> None:
    assert ast101 == parsers.parse_from_str(src101)


src102 = "x: int = 42"
ast102 = ([TypedVar(id='x', ty=IntType(), value=IntCst(value=42))], None)

def test_parse_from_str102() -> None:
    assert ast102 == parsers.parse_from_str(src102)


src103 = "b: bool = False"
ast103 = ([TypedVar(id='b', ty=BoolType(), value=BoolCst(value=False))], None)

def test_parse_from_str103() -> None:
    assert ast103 == parsers.parse_from_str(src103)


src104 = "s: str = 'azerty'"
ast104 = ([TypedVar(id='s', ty=StrType(), value=StrCst(value='azerty'))], None)

def test_parse_from_str104() -> None:
    assert ast104 == parsers.parse_from_str(src104)


src105 = "n: None = None"
ast105 = ([TypedVar(id='n', ty=NoneType(), value=NoneCst())], None)

def test_parse_from_str105() -> None:
    assert ast105 == parsers.parse_from_str(src105)


src106 = "(x, y) = (3, 4)"
ast106 = ([InitVars(ids=['x', 'y'], value=Tuple(exps=[IntCst(value=3), IntCst(value=4)]))], None)

def test_parse_from_str106() -> None:
    assert ast106 == parsers.parse_from_str(src106)


src107 = "l = [1, 2, 3]"
ast107 = ([InitVar(id='l', value=List(exps=[IntCst(value=1), IntCst(value=2), IntCst(value=3)]))], None)

def test_parse_from_str107() -> None:
    assert ast107 == parsers.parse_from_str(src107)


src108 = "l[1]"
ast108 = ([], (Subscript(Var(id='l'), IntCst(1))))

def test_parse_from_str108() -> None:
    assert ast108 == parsers.parse_from_str(src108)


src109 = "[*l, 4]"
ast109 = ([], List(exps=[Spread(operand=Var(id='l')), IntCst(value=4)]))

def test_parse_from_str109() -> None:
    assert ast109 == parsers.parse_from_str(src109)


src110 = "l[1:3]"
ast110 = ([], Slice(value=Var(id='l'), lower=IntCst(value=1), upper=IntCst(value=3)))

def test_parse_from_str110() -> None:
    assert ast110 == parsers.parse_from_str(src110)


src111 = "l[1:]"
ast111 = ([], Slice(value=Var(id='l'), lower=IntCst(value=1), upper=None))

def test_parse_from_str111() -> None:
    assert ast111 == parsers.parse_from_str(src111)


src112 = "a if x == y else b"
ast112 = ([], Cond(value=Var(id='a'),
                   test=Equal(left=Var(id='x'), right=Var(id='y')),
                   orelse=Var(id='b')))

def test_parse_from_str112() -> None:
    assert ast112 == parsers.parse_from_str(src112)


src113 = "r.num"
ast113 = ([], Field(id='r', attr='num'))

def test_parse_from_str113() -> None:
    assert ast113 == parsers.parse_from_str(src113)


src200 = """
def f() -> int:
    return 42
"""

ast200 = (
    [
        FunDef('f', [], [], IntType(),
               ([],
                Return(IntCst(42))))
    ], None
)

def test_parse_from_str200() -> None:
    assert ast200 == parsers.parse_from_str(src200)


src201 = """
def add(x: int, y: int) -> int:
    return x + y

add(10, 3)
"""

ast201 = (
    [
        FunDef('add', [], [('x', IntType()), ('y', IntType())], IntType(),
               ([],
                Return(Plus(Var('x'), Var('y')))))
    ],
    Call('add', [IntCst(value=10), IntCst(value=3)])
)

def test_parse_from_str201() -> None:
    assert ast201 == parsers.parse_from_str(src201)


src202 = """
def pos(x: int) -> bool:
    if x >= 0:
        return True
    else:
        return False
"""

ast202 = (
    [
        FunDef('pos', [], [('x', IntType())], BoolType(),
               ([],
                IfThenElse(GreaterEq(Var('x'), IntCst(0)),
                           ([],
                            Return(BoolCst(True))),
                           ([],
                            Return(BoolCst(False))))
                ))
    ], None
)

def test_parse_from_str202() -> None:
    assert ast202 == parsers.parse_from_str(src202)


src203 = """
def identity[A](x: A) -> A:
    return x
"""

ast203 = (
    [
        FunDef('identity', ['A'], [('x', TypeName('A'))], TypeName('A'),
               ([],
                Return(Var('x'))
                ))
    ], None
)

def test_parse_from_str203() -> None:
    assert ast203 == parsers.parse_from_str(src203)


src204 = """
def is_empty[A](l: list[A]) -> bool:
    match l:
        case [_, *_]:
            return False
        case _:
            return True
"""

ast204 = (
    [
        FunDef('is_empty', ['A'], [('l', ListType(TypeName('A')))], BoolType(),
               ([],
                MatchList(
                    Var('l'),
                    ([],
                     Return(BoolCst(True))),
                    '_', '_',
                    ([],
                     Return(BoolCst(False))))
                ))
    ], None
)

def test_parse_from_str204() -> None:
    assert ast204 == parsers.parse_from_str(src204)


src205 = "identity : Callable[[A], A] = lambda x: x"

ast205 = (
    [
        TypedVar(id='identity', ty=FunType(argtypes=[TypeName(id='A')], returns=TypeName(id='A')),
                 value=Lambda(args=['x'], body=Var(id='x')))
    ], None
)

def test_parse_from_str205() -> None:
    assert ast205 == parsers.parse_from_str(src205)


src206 = """
def f() -> int:
    raise SyntaxError
"""

ast206 = (
    [
        FunDef(id='f', tps=[], args=[], ret=IntType(),
               body=([], Raise(exn='SyntaxError', exps=[])))
    ], None
)

def test_parse_from_str206() -> None:
    assert ast206 == parsers.parse_from_str(src206)


src207 = """
def g() -> int:
    try:
        return f()
    except SyntaxError as e:
        return 0
"""

ast207 = (
    [
        FunDef('g', [], [], IntType(),
               ([],
                TryExcept(
                   ([],
                    Return(Call('f', []))),
                   'SyntaxError', 'e',
                   ([],
                    Return(IntCst(0))
                    ))
                ))
    ], None
)

def test_parse_from_str207() -> None:
    assert ast207 == parsers.parse_from_str(src207)


src300 = """
@dataclass
class Rational: num: int; denom: int
"""

ast300 = (
    [
        DataClass(id='Rational', tps=[], fields=[('num', IntType()), ('denom', IntType())])
    ], None
)

def test_parse_from_str300() -> None:
    assert ast300 == parsers.parse_from_str(src300)


src301 = "Rational(num=3, denom=7)"
ast301 = ([], Record(id='Rational', kwargs=[('num', IntCst(value=3)), ('denom', IntCst(value=7))]))

def test_parse_from_str301() -> None:
    assert ast301 == parsers.parse_from_str(src301)


src302 = """
def to_tuple(r: Rational) -> tuple[int, int]:
    match r:
        case Rational(num=x, denom=y):
            return (x, y)
 """

ast302 = (
    [
        FunDef('to_tuple', [], [('r', TypeName('Rational'))], TupleType([IntType(), IntType()]),
               ([],
                MatchData(
                    Var('r'),
                    [
                        ('Rational', [('num', 'x'), ('denom', 'y')],
                         ([],
                          Return(Tuple([Var('x'), Var('y')]))))
                    ])
                ))
    ], None
)

def test_parse_from_str302() -> None:
    assert ast302 == parsers.parse_from_str(src302)


src303 = """replace(r, denom=10)"""
ast303 = ([], Replace(value=Var(id='r'), kwargs=[('denom', IntCst(value=10))]))

def test_parse_from_str303() -> None:
    assert ast303 == parsers.parse_from_str(src303)


src304 = """
type primitive = IntValue | StrValue
"""

ast304 = (
    [
        TypeAlias('primitive',
                  [],
                  UnionType(
                      [
                          TypeName('IntValue'),
                          TypeName('StrValue')
                      ]))
    ], None
)

def test_parse_from_str304() -> None:
    assert ast304 == parsers.parse_from_str(src304)


src305 = """
type Tree[A] = Leaf[A] | LNode[A]
"""

ast305 = (
    [
        TypeAlias('Tree',
                  ['A'],
                  UnionType(
                      [
                          ParamType('Leaf', [TypeName('A')]),
                          ParamType('LNode', [TypeName('A')])
                      ]))
    ], None
)

def test_parse_from_str305() -> None:
    assert ast305 == parsers.parse_from_str(src305)


src306 = """
@dataclass
class Leaf[A]: 
    value: A
"""

ast306 = (
    [
        DataClass('Leaf',
                  ['A'],
                  [
                      ('value', TypeName('A'))
                  ])
    ], None
)

def test_parse_from_str306() -> None:
    assert ast306 == parsers.parse_from_str(src306)


src307 = """
@dataclass
class LNode[A]: 
    left: Tree[A]; 
    right: Tree[A]
"""

ast307 = (
    [
        DataClass('LNode',
                  ['A'],
                  [
                      ('left', ParamType('Tree', [TypeName('A')])),
                      ('right', ParamType('Tree', [TypeName('A')]))
                  ])
    ], None
)

def test_parse_from_str307() -> None:
    assert ast307 == parsers.parse_from_str(src307)


src308 = """
def size(t: Tree[int]) -> int:
    match t:
        case Leaf(value=_):
            return 1
        case LNode(left=l, right=r):
            return 1 + max(size(l), size(r))
"""

ast308 = (
    [
        FunDef('size', [], [('t', ParamType('Tree', [IntType()]))], IntType(),
               ([],
                MatchData(
                    Var(id='t'),
                    [
                        ('Leaf', [('value', '_')],
                         ([],
                          Return(IntCst(1)))),
                        ('LNode', [('left', 'l'), ('right', 'r')],
                         ([],
                          Return(
                              Plus(
                                  IntCst(1),
                                  Call('max',
                                       [
                                           Call('size', [Var('l')]),
                                           Call('size', [Var('r')])
                                       ]
                                       )))))
                    ])))
    ], None
)

def test_parse_from_str308() -> None:
    assert ast308 == parsers.parse_from_str(src308)


src400 = "import util"
ast400 = ([Import(module='util')], None)

def test_parse_from_str400() -> None:
    assert ast400 == parsers.parse_from_str(src400)


src401 = "from util import make, build"
ast401 = ([ImportFrom(module='util', names=['make', 'build'])], None)

def test_parse_from_str401() -> None:
    assert ast401 == parsers.parse_from_str(src401)


if __name__ == '__main__':
    print(util.display(parsers.parse_from_str(src307)))

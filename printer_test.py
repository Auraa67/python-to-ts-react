"""Tests for the printer module."""
import parsers
import printer

from absyn import (
    AnyType, Import, ImportFrom, NoneType, IntType, BoolType, StrType,
    ListType, Subscript, TupleType, UnionType, FunType, TypeName, ParamType,
    NoneCst, BoolCst, IntCst, StrCst, Var, Plus, Times, Minus,
    Is, Equal, Greater, GreaterEq, Less, LessEq, And, Or, Not, Cond,
    Call, Spread, Field, Lambda, List, Tuple, Record, Replace, Slice,
    IfThenElse, MatchList, MatchData, Return, Raise, TryExcept,
    InitVar, InitVars, TypedVar, FunDef, TypeAlias, DataClass,
)


# Test str_of_typ

def test_str_of_typ_any() -> None:
    assert printer.str_of_typ(AnyType()) == "any"


def test_str_of_typ_none() -> None:
    assert printer.str_of_typ(NoneType()) == "undefined"


def test_str_of_typ_int() -> None:
    assert printer.str_of_typ(IntType()) == "number"


def test_str_of_typ_bool() -> None:
    assert printer.str_of_typ(BoolType()) == "boolean"


def test_str_of_typ_str() -> None:
    assert printer.str_of_typ(StrType()) == "string"


def test_str_of_typ_list() -> None:
    assert printer.str_of_typ(ListType(IntType())) == "number[]"


def test_str_of_typ_tuple() -> None:
    assert printer.str_of_typ(TupleType([IntType(), StrType()])) == "[number, string]"


def test_str_of_typ_union() -> None:
    assert printer.str_of_typ(UnionType([IntType(), StrType()])) == "number | string"


def test_str_of_typ_funtype() -> None:
    assert printer.str_of_typ(FunType([IntType()], BoolType())) == "(arg0: number) => boolean"


def test_str_of_typ_paramtype() -> None:
    assert printer.str_of_typ(ParamType("Tree", [TypeName("A")])) == "Tree<A>"


def test_str_of_typ_typename() -> None:
    assert printer.str_of_typ(TypeName("MyType")) == "MyType"


# Test str_of_exp

def test_str_of_exp_var() -> None:
    assert printer.str_of_exp(Var("x")) == "x"


def test_str_of_exp_nonecst() -> None:
    assert printer.str_of_exp(NoneCst()) == "undefined"


def test_str_of_exp_boolcst_true() -> None:
    assert printer.str_of_exp(BoolCst(True)) == "true"


def test_str_of_exp_boolcst_false() -> None:
    assert printer.str_of_exp(BoolCst(False)) == "false"


def test_str_of_exp_intcst() -> None:
    assert printer.str_of_exp(IntCst(42)) == "42"


def test_str_of_exp_strcst() -> None:
    assert printer.str_of_exp(StrCst("hello")) == '"hello"'


def test_str_of_exp_plus() -> None:
    result = printer.str_of_exp(Plus(IntCst(1), IntCst(2)))
    assert result == "(1 + 2)"


def test_str_of_exp_times() -> None:
    result = printer.str_of_exp(Times(IntCst(2), IntCst(3)))
    assert result == "(2 * 3)"


def test_str_of_exp_minus() -> None:
    result = printer.str_of_exp(Minus(IntCst(5), IntCst(3)))
    assert result == "(5 - 3)"


def test_str_of_exp_is() -> None:
    result = printer.str_of_exp(Is(Var("x"), Var("y")))
    assert result == "(x === y)"


def test_str_of_exp_equal() -> None:
    result = printer.str_of_exp(Equal(Var("x"), Var("y")))
    assert result == "(x == y)"


def test_str_of_exp_less() -> None:
    result = printer.str_of_exp(Less(Var("x"), Var("y")))
    assert result == "(x < y)"


def test_str_of_exp_lesseq() -> None:
    result = printer.str_of_exp(LessEq(Var("x"), Var("y")))
    assert result == "(x <= y)"


def test_str_of_exp_greater() -> None:
    result = printer.str_of_exp(Greater(Var("x"), Var("y")))
    assert result == "(x > y)"


def test_str_of_exp_greatereq() -> None:
    result = printer.str_of_exp(GreaterEq(Var("x"), Var("y")))
    assert result == "(x >= y)"


def test_str_of_exp_and() -> None:
    result = printer.str_of_exp(And(BoolCst(True), BoolCst(False)))
    assert result == "(true && false)"


def test_str_of_exp_or() -> None:
    result = printer.str_of_exp(Or(BoolCst(True), BoolCst(False)))
    assert result == "(true || false)"


def test_str_of_exp_not() -> None:
    result = printer.str_of_exp(Not(BoolCst(True)))
    assert result == "(!true)"


def test_str_of_exp_cond() -> None:
    result = printer.str_of_exp(Cond(value=IntCst(1), test=BoolCst(True), orelse=IntCst(2)))
    assert result == "(true ? 1 : 2)"


def test_str_of_exp_call() -> None:
    result = printer.str_of_exp(Call("myFunc", [IntCst(1), IntCst(2)]))
    assert result == "myFunc(1, 2)"


def test_str_of_exp_call_print() -> None:
    result = printer.str_of_exp(Call("print", [StrCst("hello")]))
    assert result == 'console.log("hello")'


def test_str_of_exp_call_str() -> None:
    result = printer.str_of_exp(Call("str", [IntCst(42)]))
    assert result == "42.toString()"


def test_str_of_exp_lambda() -> None:
    result = printer.str_of_exp(Lambda(["x"], Plus(Var("x"), IntCst(1))))
    assert result == "((x) => (x + 1))"


def test_str_of_exp_tuple() -> None:
    result = printer.str_of_exp(Tuple([IntCst(1), IntCst(2)]))
    assert result == "[1, 2]"


def test_str_of_exp_list() -> None:
    result = printer.str_of_exp(List([IntCst(1), IntCst(2)]))
    assert result == "[1, 2]"


def test_str_of_exp_subscript() -> None:
    result = printer.str_of_exp(Subscript(Var("arr"), IntCst(0)))
    assert result == "arr[0]"


def test_str_of_exp_slice_with_upper() -> None:
    result = printer.str_of_exp(Slice(Var("arr"), IntCst(1), IntCst(3)))
    assert result == "arr.slice(1, 3)"


def test_str_of_exp_slice_without_upper() -> None:
    result = printer.str_of_exp(Slice(Var("arr"), IntCst(1), None))
    assert result == "arr.slice(1)"


def test_str_of_exp_spread() -> None:
    result = printer.str_of_exp(Spread(Var("arr")))
    assert result == "...arr"


def test_str_of_exp_record() -> None:
    result = printer.str_of_exp(Record("Point", [("x", IntCst(3)), ("y", IntCst(5))]))
    assert result == '{ kind: "Point", value: { x: 3, y: 5 } }'


def test_str_of_exp_field() -> None:
    result = printer.str_of_exp(Field("obj", "prop"))
    assert result == "obj.prop"


def test_str_of_exp_replace() -> None:
    result = printer.str_of_exp(Replace(Var("pt"), [("x", IntCst(10))]))
    assert result == "{...pt, x: 10}"


# Test str_of_comm

def test_str_of_comm_return() -> None:
    result = printer.str_of_comm(0, Return(IntCst(42)))
    assert "return 42;" in result


def test_str_of_comm_raise() -> None:
    result = printer.str_of_comm(0, Raise("TypeError", [StrCst("error")]))
    assert 'throw new TypeError("error");' in result


def test_str_of_comm_if_then_else() -> None:
    result = printer.str_of_comm(0, IfThenElse(
        test=Greater(Var("x"), IntCst(0)),
        body=([], Return(BoolCst(True))),
        orelse=([], Return(BoolCst(False)))
    ))
    assert "if (x > 0)" in result
    assert "return true;" in result
    assert "return false;" in result


def test_str_of_comm_matchlist() -> None:
    result = printer.str_of_comm(0, MatchList(
        subject=Var("l"),
        ifempty=([], Return(IntCst(0))),
        hd="h",
        tl="t",
        orelse=([], Return(IntCst(1)))
    ))
    assert "l.length === 0" in result
    assert "const h = l[0];" in result
    assert "const t = l.slice(1);" in result


def test_str_of_comm_matchdata() -> None:
    result = printer.str_of_comm(0, MatchData(
        subject=Var("r"),
        cases=[("Rational", [("num", "x"), ("denom", "y")], ([], Return(Var("x"))))]
    ))
    assert 'r.kind === "Rational"' in result
    assert "const { num: x, denom: y } = r.value;" in result


def test_str_of_comm_tryexcept() -> None:
    result = printer.str_of_comm(0, TryExcept(
        body=([], Return(Call("f", []))),
        exn="TypeError",
        name="err",
        handler=([], Return(IntCst(0)))
    ))
    assert "try {" in result
    assert "catch (err)" in result
    assert "err instanceof TypeError" in result


# Test str_of_decl

def test_str_of_decl_initvar() -> None:
    result = printer.str_of_decl(0, InitVar("x", IntCst(42)))
    assert "const x = 42" in result


def test_str_of_decl_typedvar() -> None:
    result = printer.str_of_decl(0, TypedVar("x", IntType(), IntCst(42)))
    assert "const x: number = 42" in result


def test_str_of_decl_import() -> None:
    result = printer.str_of_decl(0, Import("util"))
    assert 'import * as util from "./util";' in result


def test_str_of_decl_import_ignored() -> None:
    result = printer.str_of_decl(0, Import("typing"))
    assert result == ""


def test_str_of_decl_importfrom() -> None:
    result = printer.str_of_decl(0, ImportFrom("util", ["foo", "bar"]))
    assert 'import { foo, bar } from "./util";' in result


def test_str_of_decl_initvars() -> None:
    result = printer.str_of_decl(0, InitVars(["x", "y"], IntCst(0)))
    assert "let x=0, y=0;" in result


def test_str_of_decl_fundef() -> None:
    result = printer.str_of_decl(0, FunDef(
        id="add",
        tps=[],
        args=[("x", IntType()), ("y", IntType())],
        ret=IntType(),
        body=([], Return(Plus(Var("x"), Var("y"))))
    ))
    assert "function add(x: number, y: number): number {" in result
    assert "return (x + y);" in result


def test_str_of_decl_fundef_with_typeparams() -> None:
    result = printer.str_of_decl(0, FunDef(
        id="identity",
        tps=["A"],
        args=[("x", TypeName("A"))],
        ret=TypeName("A"),
        body=([], Return(Var("x")))
    ))
    assert "function identity<A>(x: A): A {" in result


def test_str_of_decl_dataclass() -> None:
    result = printer.str_of_decl(0, DataClass("Point", [], [("x", IntType()), ("y", IntType())]))
    assert "interface Point{" in result
    assert "x: number;" in result
    assert "y: number;" in result


def test_str_of_decl_typealias() -> None:
    result = printer.str_of_decl(0, TypeAlias("MyInt", [], IntType()))
    assert "type MyInt = number;" in result


# Test str_of_prog

def test_str_of_prog_empty() -> None:
    result = printer.str_of_prog(([], None))
    assert result == ""


def test_str_of_prog_with_exp() -> None:
    result = printer.str_of_prog(([], IntCst(42)))
    assert "42" in result


def test_str_of_prog_with_decls() -> None:
    result = printer.str_of_prog(([InitVar("x", IntCst(1))], None))
    assert "const x = 1" in result


# Integration tests - parse and print

def test_integration_function() -> None:
    src = """
def add(x: int, y: int) -> int:
    return x + y
"""
    prog = parsers.parse_from_str(src)
    result = printer.str_of_prog(prog)
    assert "function add(x: number, y: number): number {" in result
    assert "return (x + y);" in result


def test_integration_matchlist_formatting() -> None:
    """Test that MatchList generates proper spacing around equals sign."""
    src = """
def concat(l1: list[int], l2: list[int]) -> list[int]:
    match l1:
        case [h, *t]:
            return [h, *concat(t, l2)]
        case _:
            return l2
"""
    prog = parsers.parse_from_str(src)
    result = printer.str_of_prog(prog)
    # Verify proper spacing: "const h = " instead of "const h= "
    assert "const h = l1[0];" in result
    assert "const t = l1.slice(1);" in result


def test_integration_dataclass() -> None:
    src = """
@dataclass
class Point: x: int; y: int
"""
    prog = parsers.parse_from_str(src)
    result = printer.str_of_prog(prog)
    assert "interface Point{" in result
    assert "x: number;" in result


def test_integration_raise() -> None:
    src = """
def f() -> int:
    raise ValueError("error")
"""
    prog = parsers.parse_from_str(src)
    result = printer.str_of_prog(prog)
    assert 'throw new ValueError("error");' in result


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, "-v"])

from dataclasses import dataclass
from collections.abc import Callable

type Tree[A] = Empty[A] | LNode[A]


@dataclass
class Empty[A]:
    pass


@dataclass
class LNode[A]:
    left: Tree[A]
    right: Tree[A]


type int_Tree = Tree[int]
type int_list = list[int]
type int_bool_tuple = tuple[int, bool]
type nothing = None
type call = Callable[[int, bool], str]

x = 3
y: int = 9
(a, b) = (x + y * 7 - 10, 9)
d = (1, 2, 3, 4)
e = [1, 2, 3, 4]
c = [*e]


# g = f(1,2,3,4)
# h = m.f(1,2,3,4)

em: Tree[int] = Empty()
no: Tree[int] = LNode(left=Empty(), right=Empty())


def f(x: int) -> str:
    return str(x)


def size[A](t: Tree[A]) -> int:
    match t:
        case Empty(): return 0
        case LNode(left=_, right=r): return 1


def head(l: list[int]) -> int:
    match l:
        case [h, *t]: return h
        case _: return 0


def times(x: int, y: int) -> int:
    if x == 0:
        return 0
    else:
        return x * y


def handle(x: int, y: str) -> str:
    try:
        raise IndexError()
    except Exception as err:
        return y


def is_empty[A](l: list[A]) -> bool:
    match (l):
        case [_, *_]:
            return True
        case _:
            return False


def concat[A](l1: list[A], l2: list[A]) -> list[A]:
    match (l1):
        case [h1, *t1]:
            return [h1, *concat(t1, l2)]
        case _:
            return l2

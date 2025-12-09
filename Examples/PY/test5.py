from dataclasses import dataclass
from collections.abc import Callable
type Tree[A, B] = Leaf[A, B] | LNode[A, B]
@dataclass
class Leaf[A, B]:
    value: A
@dataclass
class LNode[A, B]:
    value: B
    left: Tree[A, B]
    right: Tree[A, B]
def max(x: int, y: int) -> int:
    if x > y:
        return x
    else:
        return y
def size(t: Tree[int, bool]) -> int:
    match t:
        case Leaf(value=_):
            return 1
        case LNode(value=x, left=l, right=r):
            return max(size(l), size(r))
        case _:
            return 1
def length[A](l: list[A]) -> int:
    match l:
        case [h, *t]:
            return 1 + (length(t))
        case _:
            return 0
def concat[A](l1: list[A], l2: list[A]) -> list[A]:
    match l1:
        case [h, *t]:
            return [h, *(concat(t, l2))]
        case _:
            return l2
def first[A, B](z: tuple[A, B]) -> A:
    (x, y) = z
    return x
def f5[A, B, C](f: Callable[[A], B], g: Callable[[B], C]) -> Callable[[A], C]:
    return lambda x: g(f(x))
def combine[A, B](l1: list[A], l2: list[B]) -> list[tuple[A, B]]:
    match l1:
        case [h1, *t1]:
            match l2:
                case [h2, *t2]:
                    return [(h1, h2), *(combine(t1, t2))]
                case _:
                    return []
        case _:
            return []
def split[A, B](l: list[tuple[A, B]]) -> tuple[list[A], list[B]]:
    match l:
        case [h, *t]:
            (l1, l2) = split(t)
            (h1, h2) = h
            return ([h1, *l1], [h2, *l2])
        case _:
            return ([], [])
l2 = [1, 3, 5, 7]
l3 = [(2, 1), (7, 2)]
l4: list[tuple[str, int]] = [("e", 1), ("kjh", 2)]
l: list[int] = []

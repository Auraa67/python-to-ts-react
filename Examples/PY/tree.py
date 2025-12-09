from collections.abc import Callable
from dataclasses import dataclass
from test14 import string_of_int
type Tree[A] = Leaf[A] | LNode[A]
@dataclass
class Leaf[A]:
    value: A
@dataclass
class LNode[A]:
    left: Tree[A]
    right: Tree[A]
type Tree2[A, B] = Leaf[A] | Node2[A, B]
@dataclass
class Node2[A, B]:
    left: Tree2[A, B]
    right: Tree2[A, B]
def size[A](t: Tree[A]) -> int:
    match t:
        case Leaf(value=_):
            return 1
        case LNode(left=l, right=r):
            return (size(l)) + (size(r))
def length[A](l: list[A]) -> int:
    match l:
        case [_, *t]:
            return 1 + (length(t))
        case _:
            return 0
def is_empty[A](l: list[A]) -> bool:
    match l:
        case [_, *_]:
            return False
        case _:
            return True
def hd[A](l: list[A]) -> A:
    match l:
        case [h, *t]:
            return h
        case _:
            raise ValueError
def tl[A](l: list[A]) -> list[A]:
    match l:
        case [h, *t]:
            return t
        case _:
            raise ValueError
def join(l: list[str], delim: str) -> str:
    match l:
        case [h, *t]:
            if is_empty(t):
                return h
            else:
                return (h + delim) + (join(t, delim))
        case _:
            return ""
def concat[A](l1: list[A], l2: list[A]) -> list[A]:
    match l1:
        case [h1, *t1]:
            return [h1, *(concat(t1, l2))]
        case _:
            return l2
def to_list[A](t: Tree[A]) -> list[A]:
    match t:
        case Leaf(value=v):
            return [v]
        case LNode(left=l, right=r):
            return [*(to_list(l)), *(to_list(r))]
def reverse[A](l: list[A]) -> list[A]:
    match l:
        case [h, *t]:
            return [*(reverse(t)), h]
        case _:
            return []
def unzip[A, B](l: list[tuple[A, B]]) -> tuple[list[A], list[B]]:
    match l:
        case [h, *t]:
            (h1, h2) = h
            (t1, t2) = unzip(t)
            return ([h1, *t1], [h2, *t2])
        case _:
            return ([], [])
def map[A, B](f: Callable[[A], B], l: list[A]) -> list[B]:
    match l:
        case [hd, *tl]:
            return [f(hd), *(map(f, tl))]
        case _:
            return []
def fold_left[A, B](f: Callable[[A, B], A], init: A, l: list[B]) -> A:
    match l:
        case [h, *t]:
            return fold_left(f, f(init, h), t)
        case _:
            return init
l = Leaf(value=17)
t = LNode(left=Leaf(value=5), right=LNode(left=Leaf(value=3), right=Leaf(value=7)))
lst = [21, 43, 56]
s = length(lst)
l3: list[tuple[int, int]] = [(21, 43), (56, 78)]
s42 = string_of_int(42)

print(s42)

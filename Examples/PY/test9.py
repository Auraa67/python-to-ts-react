from collections.abc import Callable
from dataclasses import dataclass
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
def first[A, B](z: tuple[A, B]) -> A:
    (x, _) = z
    return x
def size(t: Tree[int, str]) -> int:
    match t:
        case Leaf(value=_):
            return 1
        case LNode(value=_, left=l, right=r):
            return 1 + (max(size(l), size(r)))
def simple(t: Tree[int, str]) -> bool:
    match t:
        case Leaf(value=_):
            return True
        case _:
            return False
def compose[A, B, C](f: Callable[[A], B], g: Callable[[B], C]) -> Callable[[A], C]:
    return lambda x: g(f(x))
def succ(x: int) -> int:
    return x + 1
def string_of_int(x: int) -> str:
    return str(x)
f = compose(succ, string_of_int)
l: Tree[int, str] = Leaf(value=2)
t: Tree[int, str] = LNode(value="ok", left=Leaf(value=3), right=Leaf(value=5))

print(size(t))

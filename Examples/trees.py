from dataclasses import dataclass

type Tree[A, B] = Leaf[A] | LNode[A, B]

@dataclass
class Leaf[A]: value: A

@dataclass
class LNode[A, B]: value: B; left: Tree[A, B]; right: Tree[A, B]


def mkLeaf[A](value: A) -> Leaf[A]:
    return Leaf(value=value)


def mkLNode[A, B](value: B, left: Tree[A, B], right: Tree[A, B]) -> LNode[A, B]:
    return LNode(value=value, left=left, right=right)


def max(x: int, y: int) -> int:
    if x > y:
        return x
    else:
        return y


def size(t: Tree[int, str]) -> int:
    match t:
        case Leaf(value=_):
            return 1
        case LNode(value=_, left=l, right=r):
            return 1 + max(size(l), size(r))


t: Tree[int, str] = mkLNode("ok", mkLeaf(3), mkLeaf(5))

s = size(t)
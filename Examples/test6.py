from dataclasses import dataclass

type MyList[A] = MyNil[A] | MyCons[A]


@dataclass
class MyNil[A]:
    pass


@dataclass
class MyCons[A]:
    hd: A
    tl: MyList[A]


type Colour = Red | Black | White


@dataclass
class Red:
    pass


@dataclass
class Black:
    pass


@dataclass
class White:
    pass


type Tree[A, C] = Leaf[A, C] | LNode[A, C]


@dataclass
class Leaf[A, C]:
    value: A


@dataclass
class LNode[A, C]:
    value: C
    left: Tree[A, C]
    right: Tree[A, C]


def toInt(c: Colour) -> int:
    match c:
        case Red():
            return 0
        case Black():
            return 1
        case White():
            return 2


def length[A](l: MyList[A]) -> int:
    match l:
        case MyNil():
            return 0
        case MyCons(hd=_, tl=t):
            return 1 + length(t)


def max(x: int, y: int) -> int:
    if x > y:
        return x
    else:
        return y


def size[A, B](t: Tree[A, B]) -> int:
    match t:
        case Leaf(value=_):
            return 1
        case LNode(value=_, left=l, right=r):
            return max(size(l), size(r))


c = Red()
l: Tree[int, str] = Leaf(value=3)
t = LNode(value="abc", left=Leaf(value=7), right=Leaf(value=size(l)))

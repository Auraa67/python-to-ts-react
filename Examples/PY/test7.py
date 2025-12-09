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
type Tree[A, B] = Leaf[A, B] | Node2[A, B]
@dataclass
class Leaf[A, B]:
    value: A
@dataclass
class Node2[A, B]:
    value: B
    left: Tree[A, B]
    right: Tree[A, B]
@dataclass
class Point:
    x: int
    y: int
@dataclass
class Pair[A, B]:
    fst: A
    snd: B
p: Pair[int, str] = Pair(fst=4, snd="something")
p1 = p.fst
p2 = p.snd
def a() -> int:
    match p:
        case Pair(fst=f, snd=s):
            return f
def b() -> str:
    match p:
        case Pair(fst=f, snd=s):
            return s
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
        case MyCons(hd=h, tl=t):
            return 1 + (length(t))
def max(x: int, y: int) -> int:
    if x > y:
        return x
    else:
        return y
def size[A, B](t: Tree[A, B]) -> int:
    match t:
        case Leaf(value=_):
            return 1
        case Node2(value=_, left=l, right=r):
            return max(size(l), size(r))
def copy(t: Tree[int, str]) -> Tree[int, str]:
    match t:
        case Leaf(value=a):
            return Leaf(value=a)
        case Node2(value=b, left=l, right=r):
            l2 = copy(l)
            r2 = copy(r)
            return Node2(value=b, left=l2, right=r2)
c: Colour = Red()
l: Tree[int, str] = Leaf(value=3)
t: Tree[int, str] = Node2(value="abc", left=Leaf(value=7), right=Leaf(value=size(l)))

from dataclasses import dataclass
type MyList[A] = Nil[A] | Cons[A]
@dataclass
class Nil[A]:
    pass
@dataclass
class Cons[A]:
    hd: A
    tl: MyList[A]
def length[A](l: MyList[A]) -> int:
    match l:
        case Nil():
            return 0
        case Cons(hd=_, tl=t):
            return 1 + (length(t))
def to_list[A](l: MyList[A]) -> list[A]:
    match l:
        case Nil():
            return []
        case Cons(hd=h, tl=t):
            return [h, *(to_list(t))]
def from_list[A](l: list[A]) -> MyList[A]:
    match l:
        case [h, *t]:
            return Cons(hd=h, tl=from_list(t))
        case _:
            return Nil()
l = from_list(["a", "b", "c", "d", "e"])
r = to_list(l)

print(r)

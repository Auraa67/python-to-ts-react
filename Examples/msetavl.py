from collections.abc import Callable
from dataclasses import dataclass

type Comparaison = Eq | Lt | Gt

@dataclass
class Eq: pass

@dataclass
class Lt: pass

@dataclass
class Gt: pass


type Tree[A] = Empty[A] | Node2[A]

@dataclass
class Empty[A]:
    pass

@dataclass
class Node2[A]:
    height: int
    left: Tree[A]
    value: A
    right: Tree[A]


def check(res: int) -> Comparaison:
    if res == 0:
        return Eq()
    else:
        if res < 0:
            return Lt()
        else:
            return Gt()


def max(i: int, j: int) -> int:
    if i > j:
        return i
    else:
        return j


def get_or_else[A](v: A | None, other: A) -> A:
    if v is None:
        return other
    else:
        return v


def is_empty[A](t: Tree[A]) -> bool:
    match t:
        case Empty():
            return True
        case _:
            return False


def mem[A](x: A, t: Tree[A], cmp: Callable[[A, A], int]) -> bool:
    match t:
        case Empty():
            return False
        case Node2(height=_, left=l, value=k, right=r):
            match check(cmp(x, k)):
                case Eq():
                    return True
                case Lt():
                    return mem(x, l, cmp)
                case Gt():
                    return mem(x, r, cmp)


def find[A](x: A, t: Tree[A], cmp: Callable[[A, A], int]) -> A | None:
    match t:
        case Empty():
            return None
        case Node2(height=_, left=l, value=k, right=r):
            match check(cmp(x, k)):
                case Eq():
                    return k
                case Lt():
                    return find(x, l, cmp)
                case Gt():
                    return find(x, r, cmp)


def min_elt[A](t: Tree[A]) -> A | None:
    match t:
        case Empty():
            return None
        case Node2(height=_, left=l, value=x, right=_):
            match l:
                case Empty():
                    return x
                case Node2(height=_, left=_, value=_, right=_):
                    return min_elt(l)


def max_elt[A](t: Tree[A]) -> A | None:
    match t:
        case Empty():
            return None
        case Node2(height=_, left=_, value=x, right=r):
            match r:
                case Empty():
                    return x
                case Node2(height=_, left=_, value=_, right=_):
                    return max_elt(r)


def height[A](t: Tree[A]) -> int:
    match t:
        case Empty():
            return 0
        case Node2(height=h, left=_, value=_, right=_):
            return h


def size[A](t: Tree[A]) -> int:
    match t:
        case Empty():
            return 0
        case Node2(height=_, left=l, value=_, right=r):
            return size(l) + size(r) + 1


def create[A](l: Tree[A], x: A, r: Tree[A]) -> Tree[A]:
    hl: int = height(l)
    hr: int = height(r)
    return Node2(height=(max(hl, hr) + 1), left=l, value=x, right=r)


def leaf[A](x: A) -> Tree[A]:
    return create(Empty(), x, Empty())


def bal[A](l: Tree[A], x: A, r: Tree[A]) -> Tree[A]:
    hl: int = height(l)
    hr: int = height(r)
    if (hr + 2) < hl:
        match l:
            case Empty():
                raise SystemExit
            case Node2(height=_, left=ll, value=lx, right=lr):
                if not (height(lr) > height(ll)):
                    rs = create(lr, x, r)
                    return create(ll, lx, rs)
                else:
                    match lr:
                        case Empty():
                            raise SystemExit
                        case Node2(height=_, left=lrl, value=lrx, right=lrr):
                            ls = create(ll, lx, lrl)
                            rs = create(lrr, x, r)
                            return create(ls, lrx, rs)
    else:
        if (hl + 2) < hr:
            match r:
                case Empty():
                    raise SystemExit
                case Node2(height=_, left=rl, value=rx, right=rr):
                    if not (height(rl) > height(rr)):
                        ls = create(l, x, rl)
                        return create(ls, rx, rr)
                    else:
                        match rl:
                            case Empty():
                                raise SystemExit
                            case Node2(height=_, left=rll, value=rlx, right=rlr):
                                ls = create(l, x, rll)
                                rs = create(rlr, rx, rr)
                                return create(ls, rlx, rs)
        else:
            return create(l, x, r)


def add[A](x: A, t: Tree[A], cmp: Callable[[A, A], int]) -> Tree[A]:
    match t:
        case Empty():
            return leaf(x)
        case Node2(height=_, left=l, value=y, right=r):
            match check(cmp(x, y)):
                case Eq():
                    return create(l, y, r)
                case Lt():
                    return bal(add(x, l, cmp), y, r)
                case Gt():
                    return bal(l, y, add(x, r, cmp))


def remove_min[A](l: Tree[A], x: A, r: Tree[A]) -> tuple[Tree[A], A]:
    match l:
        case Empty():
            return (r, x)
        case Node2(height=_, left=ll, value=lx, right=lr):
            (l2, m) = remove_min(ll, lx, lr)
            return (bal(l2, x, r), m)


def merge[A](s1: Tree[A], s2: Tree[A]) -> Tree[A]:
    match s1:
        case Empty():
            return s2
        case Node2(height=_, left=_, value=_, right=_):
            match s2:
                case Empty():
                    return s1
                case Node2(height=_, left=l2, value=x2, right=r2):
                    (s3, m) = remove_min(l2, x2, r2)
                    return bal(s1, m, s3)


def remove[A](x: A, t: Tree[A], cmp: Callable[[A, A], int]) -> Tree[A]:
    match t:
        case Empty():
            return Empty()
        case Node2(height=_, left=l, value=y, right=r):
            match check(cmp(x, y)):
                case Eq():
                    return merge(l, r)
                case Lt():
                    return bal(remove(x, l, cmp), y, r)
                case Gt():
                    return bal(l, y, remove(x, r, cmp))


def toList[A](t: Tree[A]) -> list[A]:
    match t:
        case Empty():
            return []
        case Node2(height=_, left=l, value=y, right=r):
            return [*toList(l), y, *toList(r)]

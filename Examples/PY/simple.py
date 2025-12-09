from collections.abc import Callable
def size[A](l: list[A]) -> int:
    match l:
        case [_, *t]:
            return 1 + (size(t))
        case _:
            return 0
def concat[A](l1: list[A], l2: list[A]) -> list[A]:
    match l1:
        case [h, *t]:
            return [h, *(concat(t, l2))]
        case _:
            return l2
def map[A, B](f: Callable[[A], B], l: list[A]) -> list[B]:
    match l:
        case [hd, *tl]:
            return [f(hd), *(map(f, tl))]
        case _:
            return []
def string_of_int(i: int) -> str:
    return str(i)
l1 = [5, 4, 3, 2, 1]
l2 = [6, 7, 8, 9, 0]
r = concat(l1, l2)
l3: list[tuple[int, int]] = [(1, 2), (3, 4), (5, 6)]
def unzip[A, B](l: list[tuple[A, B]]) -> tuple[list[A], list[B]]:
    match l:
        case [h, *t]:
            (h1, h2) = h
            (t1, t2) = unzip(t)
            return ([h1, *t1], [h2, *t2])
        case _:
            return ([], [])
(r1, r2) = unzip(l3)

print(r1, r2, map(string_of_int, r))

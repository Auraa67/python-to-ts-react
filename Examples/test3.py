from collections.abc import Callable


def length[A](l: list[A]) -> int:
    match l:
        case [h, *t]:
            return 1 + length(t)
        case _:
            return 0


x = 3
f: Callable[[list[int]], int] = (lambda l: length(l))
l: list[int] = [5, 4, 3, 2, 1]

print(f(l))

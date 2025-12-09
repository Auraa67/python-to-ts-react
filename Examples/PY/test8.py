from collections.abc import Callable
def map[A, B](f: Callable[[A], B], l: list[A]) -> list[B]:
    def map2(acc: list[B], l: list[A]) -> list[B]:
        match l:
            case [hd, *tl]:
                return map2([f(hd), *acc], tl)
            case _:
                return acc
    return map2([], l)

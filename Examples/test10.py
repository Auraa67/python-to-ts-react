from collections.abc import Callable

def fold_left[A, B](f: Callable[[A, B], A], init: A, l: list[B]) -> A:
    match l:
        case [h, *t]:
            return fold_left(f, f(init, h), t)
        case _:
            return init


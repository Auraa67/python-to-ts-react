from collections.abc import Callable


def f1(x: int) -> int:
    return x * 2


def f2(x: int, y: int) -> int:
    if x < y:
        return x
    else:
        return y


def f3(x: int) -> Callable[[int], int]:
    return (lambda y: y + x)


def f4(f: Callable[[int], bool], g: Callable[[bool], str]) -> Callable[[int], str]:
    return (lambda x: g(f(x)))


def f5[A, B, C](f: Callable[[A], B], g: Callable[[B], C]) -> Callable[[A], C]:
    return (lambda x: g(f(x)))

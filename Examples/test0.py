from collections.abc import Callable


def compose[A, B, C](f: Callable[[A], B], g: Callable[[B], C]) -> Callable[[A], C]:
    return (lambda x : g(f(x)))


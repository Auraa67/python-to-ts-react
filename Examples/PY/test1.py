from collections.abc import Callable
def f(x: int, y: int) -> Callable[[int], int]:
    return lambda z: z * (x + y)

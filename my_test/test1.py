from collections.abc import Callable

def apply_twice(f: Callable[[int], int], x: int) -> int:
	return f(f(x))

def map_inc(l: list[int]) -> list[int]:
	match l:
		case [h, *t]:
			inc = lambda x: x + 1
			return [inc(h), *map_inc(t)]
		case _:
			return []

res1 = apply_twice(lambda x: x * 2, 10)
res2 = map_inc([1, 2, 3])

print(res1)
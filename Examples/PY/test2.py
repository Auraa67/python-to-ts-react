def concat(l1: list[int], l2: list[int]) -> list[int]:
    match l1:
        case [h, *t]:
            return [h, *(concat(t, l2))]
        case _:
            return l2
x = [5, 4]
y = [8, 9, 10]
r = concat(x, y)

print(r)

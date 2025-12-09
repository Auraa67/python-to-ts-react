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
l1 = [5, 4, 3, 2, 1]
l2 = [6, 7, 8, 9, 0]
r = concat(l1, l2)

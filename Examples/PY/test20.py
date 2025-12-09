def insert[A](l: list[A], index: int, elt: A) -> list[A]:
    if (index < 0) or (index >= (len(l))):
        raise IndexError
    else:
        return [*l[0:index], elt, *l[index:]]
def update[A](l: list[A], index: int, elt: A) -> list[A]:
    if (index < 0) or (index > (len(l))):
        raise IndexError
    else:
        return [*l[0:index], elt, *l[index + 1:]]
l = [1, 2, 3, 4, 5]

print(insert(l, 3, 9))

def empty[A](l: list[A]) -> bool:
    match l:
        case [_, *_]:
            return False
        case _:
            return True

l = [1, *[2, *[3, *[]]]]

print(empty(l))
def unzip[A, B](l: list[tuple[A, B]]) -> tuple[list[A], list[B]]:
    match l:
        case [h, *t]:
            (h1, h2) = h
            (t1, t2) = unzip(t)
            return ([h1, *t1], [h2, *t2])
        case _:
            return ([], [])

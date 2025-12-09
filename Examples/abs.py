def valeur_abs(x: int) -> int:
    if x < 0:
        return x
    else:
        return 0 - x


r = valeur_abs(-5)

print(r)

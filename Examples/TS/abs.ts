function valeur_abs(x: number): number {
    if (x < 0) {
        return x;
    } else {
        return (0 - x);
    }
}
const r = valeur_abs(-5)

print(r)

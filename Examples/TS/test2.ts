function concat(l1: number[], l2: number[]): number[] {
    if (l1.length === 0) {
        return l2;
    } else {
        const h= l1[0];
        const t= l1.slice(1);
        return [h, ...concat(t, l2)];
    }
}
const x = [5, 4]
const y = [8, 9, 10]
const r = concat(x, y)

print(r)

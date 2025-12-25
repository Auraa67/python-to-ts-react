function size<A>(l: A[]): number {
    if (l.length === 0) {
        return 0;
    } else {
        const t= l.slice(1);
        return (1 + size(t));
    }
}
function concat<A>(l1: A[], l2: A[]): A[] {
    if (l1.length === 0) {
        return l2;
    } else {
        const h= l1[0];
        const t= l1.slice(1);
        return [h, ...concat(t, l2)];
    }
}
const l1 = [5, 4, 3, 2, 1]
const l2 = [6, 7, 8, 9, 0]
const r = concat(l1, l2)

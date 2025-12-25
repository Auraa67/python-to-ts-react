import { Callable } from "./collections.abc";
function size<A>(l: A[]): number {
    if (l.length === 0) {
        return 0;
    } else {
        const _= l[0];
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
function map<A, B>(f: (arg0: A) => B, l: A[]): B[] {
    if (l.length === 0) {
        return [];
    } else {
        const hd= l[0];
        const tl= l.slice(1);
        return [f(hd), ...map(f, tl)];
    }
}
function string_of_int(i: number): string {
    return str(i);
}
const l1 = [5, 4, 3, 2, 1]
const l2 = [6, 7, 8, 9, 0]
const r = concat(l1, l2)
const l3: [number, number][] = [[1, 2], [3, 4], [5, 6]]
function unzip<A, B>(l: [A, B][]): [A[], B[]] {
    if (l.length === 0) {
        return [[], []];
    } else {
        const h= l[0];
        const t= l.slice(1);
        let h1=h, h2=h;
        let t1=unzip(t), t2=unzip(t);
        return [[h1, ...t1], [h2, ...t2]];
    }
}
let r1=unzip(l3), r2=unzip(l3);

print(r1, r2, map(string_of_int, r))

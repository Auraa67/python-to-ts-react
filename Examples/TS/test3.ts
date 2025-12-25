function length<A>(l: A[]): number {
    if (l.length === 0) {
        return 0;
    } else {
        const h= l[0];
        const t= l.slice(1);
        return (1 + length(t));
    }
}
const x = 3
const f: (arg0: number[]) => number = (l) => length(l)
const l: number[] = [5, 4, 3, 2, 1]

console.log(f(l))

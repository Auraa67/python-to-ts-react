function length<A>(l: A[]): number {
    if (l.length > 0) {
        const [h, ...t] = l
        return 1 + length(t)
    } else {
        return 0
    }
}
const x = 3
const f: (_: number[]) => number = l => length(l)
const l: number[] = [5, 4, 3, 2, 1]

console.log(f(l))

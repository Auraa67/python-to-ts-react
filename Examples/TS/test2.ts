function concat(l1: number[], l2: number[]): number[] {
    if (l1.length > 0) {
        const [h, ...t] = l1
        return [h, ...concat(t, l2)]
    } else {
        return l2
    }
}
const x = [5, 4]
const y = [8, 9, 10]
const r = concat(x, y)

console.log(r)

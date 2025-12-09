export function size<A>(l: A[]): number {
    if (l.length > 0) {
        const [, ...t] = l
        return 1 + size(t)
    } else {
        return 0
    }
}

export function concat<A>(l1: A[], l2: A[]): A[] {
    if (l1.length > 0) {
        const [h, ...t] = l1
        return [h, ...concat(t, l2)]
    } else {
        return l2
    }
}
const l1 = [5, 4, 3, 2, 1]
const l2 = [6, 7, 8, 9, 0]
const r = concat(l1, l2)

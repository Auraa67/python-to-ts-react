function size<A>(l: A[]): number {
    if (l.length > 0) {
        const [, ...t] = l
        return 1 + size(t)
    } else {
        return 0
    }
}

function concat<A>(l1: A[], l2: A[]): A[] {
    if (l1.length > 0) {
        const [h, ...t] = l1
        return [h, ...concat(t, l2)]
    } else {
        return l2
    }
}

function map<A, B>(f: (_: A) => B, l: A[]): B[] {
    if (l.length > 0) {
        const [hd, ...tl] = l
        return [f(hd), ...map(f, tl)]
    } else {
        return []
    }
}

function string_of_int(i: number): string {
    return i.toString()
}
const l1 = [5, 4, 3, 2, 1]
const l2 = [6, 7, 8, 9, 0]
const r = concat(l1, l2)
const l3: [number, number][] = [[1, 2], [3, 4], [5, 6]]

function unzip<A, B>(l: [A, B][]): [A[], B[]] {
    if (l.length > 0) {
        const [h, ...t] = l
        const [h1, h2] = h
        const [t1, t2] = unzip(t)
        return [[h1, ...t1], [h2, ...t2]]
    } else {
        return [[], []]
    }
}
const [r1, r2] = unzip(l3)

console.log(r1, r2, map(string_of_int, r))

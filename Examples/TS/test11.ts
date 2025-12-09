export function unzip<A, B>(l: [A, B][]): [A[], B[]] {
    if (l.length > 0) {
        const [h, ...t] = l
        const [h1, h2] = h
        const [t1, t2] = unzip(t)
        return [[h1, ...t1], [h2, ...t2]]
    } else {
        return [[], []]
    }
}

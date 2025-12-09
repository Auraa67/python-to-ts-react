export function map<A, B>(f: (_: A) => B, l: A[]): B[] {

    function map2(acc: B[], l: A[]): B[] {
        if (l.length > 0) {
            const [hd, ...tl] = l
            return map2([f(hd), ...acc], tl)
        } else {
            return acc
        }
    }
    return map2([], l)
}

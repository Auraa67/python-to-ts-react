export function fold_left<A, B>(f: (_: A, __: B) => A, init: A, l: B[]): A {
    if (l.length > 0) {
        const [h, ...t] = l
        return fold_left(f, f(init, h), t)
    } else {
        return init
    }
}

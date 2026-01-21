function fold_left<A, B>(f: (arg0: A, arg1: B) => A, init: A, l: B[]): A {
    if (l.length === 0) {
        return init;
    } else {
        const h = l[0];
        const t = l.slice(1);
        return fold_left(f, f(init, h), t);
    }
}

export type Comparaison = Eq | Lt | Gt

export interface Eq {
    type: 'Eq'
}

export interface Lt {
    type: 'Lt'
}

export interface Gt {
    type: 'Gt'
}

export type Tree<A> = Empty<A> | Node2<A>

export interface Empty<A> {
    type: 'Empty'
}

export interface Node2<A> {
    type: 'Node2'
    height: number
    left: Tree<A>
    value: A
    right: Tree<A>
}

export function check(res: number): Comparaison {
    if (res == 0) {
        return { type: 'Eq' }
    } else {
        if (res < 0) {
            return { type: 'Lt' }
        } else {
            return { type: 'Gt' }
        }
    }
}

export function max(i: number, j: number): number {
    if (i > j) {
        return i
    } else {
        return j
    }
}

export function get_or_else<A>(v: A | undefined, other: A): A {
    if (v === undefined) {
        return other
    } else {
        return v
    }
}

export function is_empty<A>(t: Tree<A>): boolean {
    switch (t.type) {
        case 'Empty': {
            return true
        }
        default: {
            return false
        }
    }
}

export function mem<A>(x: A, t: Tree<A>, cmp: (_: A, __: A) => number): boolean {
    switch (t.type) {
        case 'Empty': {
            return false
        }
        case 'Node2': {
            const { left: l, value: k, right: r } = t
            switch (check(cmp(x, k)).type) {
                case 'Eq': {
                    return true
                }
                case 'Lt': {
                    return mem(x, l, cmp)
                }
                case 'Gt': {
                    return mem(x, r, cmp)
                }
            }
        }
    }
}

export function find<A>(x: A, t: Tree<A>, cmp: (_: A, __: A) => number): A | undefined {
    switch (t.type) {
        case 'Empty': {
            return undefined
        }
        case 'Node2': {
            const { left: l, value: k, right: r } = t
            switch (check(cmp(x, k)).type) {
                case 'Eq': {
                    return k
                }
                case 'Lt': {
                    return find(x, l, cmp)
                }
                case 'Gt': {
                    return find(x, r, cmp)
                }
            }
        }
    }
}

export function min_elt<A>(t: Tree<A>): A | undefined {
    switch (t.type) {
        case 'Empty': {
            return undefined
        }
        case 'Node2': {
            const { left: l, value: x } = t
            switch (l.type) {
                case 'Empty': {
                    return x
                }
                case 'Node2': {
                    return min_elt(l)
                }
            }
        }
    }
}

export function max_elt<A>(t: Tree<A>): A | undefined {
    switch (t.type) {
        case 'Empty': {
            return undefined
        }
        case 'Node2': {
            const { value: x, right: r } = t
            switch (r.type) {
                case 'Empty': {
                    return x
                }
                case 'Node2': {
                    return max_elt(r)
                }
            }
        }
    }
}

export function height<A>(t: Tree<A>): number {
    switch (t.type) {
        case 'Empty': {
            return 0
        }
        case 'Node2': {
            const { height: h } = t
            return h
        }
    }
}

export function size<A>(t: Tree<A>): number {
    switch (t.type) {
        case 'Empty': {
            return 0
        }
        case 'Node2': {
            const { left: l, right: r } = t
            return (size(l) + size(r)) + 1
        }
    }
}

export function create<A>(l: Tree<A>, x: A, r: Tree<A>): Tree<A> {
    const hl: number = height(l)
    const hr: number = height(r)
    return { type: 'Node2', height: max(hl, hr) + 1, left: l, value: x, right: r }
}

export function leaf<A>(x: A): Tree<A> {
    return create({ type: 'Empty' }, x, { type: 'Empty' })
}

export function bal<A>(l: Tree<A>, x: A, r: Tree<A>): Tree<A> {
    const hl: number = height(l)
    const hr: number = height(r)
    if ((hr + 2) < hl) {
        switch (l.type) {
            case 'Empty': {
                throw new Error()
            }
            case 'Node2': {
                const { left: ll, value: lx, right: lr } = l
                if (!(height(lr) > height(ll))) {
                    const rs = create(lr, x, r)
                    return create(ll, lx, rs)
                } else {
                    switch (lr.type) {
                        case 'Empty': {
                            throw new Error()
                        }
                        case 'Node2': {
                            const { left: lrl, value: lrx, right: lrr } = lr
                            const ls = create(ll, lx, lrl)
                            const rs = create(lrr, x, r)
                            return create(ls, lrx, rs)
                        }
                    }
                }
            }
        }
    } else {
        if ((hl + 2) < hr) {
            switch (r.type) {
                case 'Empty': {
                    throw new Error()
                }
                case 'Node2': {
                    const { left: rl, value: rx, right: rr } = r
                    if (!(height(rl) > height(rr))) {
                        const ls = create(l, x, rl)
                        return create(ls, rx, rr)
                    } else {
                        switch (rl.type) {
                            case 'Empty': {
                                throw new Error()
                            }
                            case 'Node2': {
                                const { left: rll, value: rlx, right: rlr } = rl
                                const ls = create(l, x, rll)
                                const rs = create(rlr, rx, rr)
                                return create(ls, rlx, rs)
                            }
                        }
                    }
                }
            }
        } else {
            return create(l, x, r)
        }
    }
}

export function add<A>(x: A, t: Tree<A>, cmp: (_: A, __: A) => number): Tree<A> {
    switch (t.type) {
        case 'Empty': {
            return leaf(x)
        }
        case 'Node2': {
            const { left: l, value: y, right: r } = t
            switch (check(cmp(x, y)).type) {
                case 'Eq': {
                    return create(l, y, r)
                }
                case 'Lt': {
                    return bal(add(x, l, cmp), y, r)
                }
                case 'Gt': {
                    return bal(l, y, add(x, r, cmp))
                }
            }
        }
    }
}

export function remove_min<A>(l: Tree<A>, x: A, r: Tree<A>): [Tree<A>, A] {
    switch (l.type) {
        case 'Empty': {
            return [r, x]
        }
        case 'Node2': {
            const { left: ll, value: lx, right: lr } = l
            const [l2, m] = remove_min(ll, lx, lr)
            return [bal(l2, x, r), m]
        }
    }
}

export function merge<A>(s1: Tree<A>, s2: Tree<A>): Tree<A> {
    switch (s1.type) {
        case 'Empty': {
            return s2
        }
        case 'Node2': {
            switch (s2.type) {
                case 'Empty': {
                    return s1
                }
                case 'Node2': {
                    const { left: l2, value: x2, right: r2 } = s2
                    const [s3, m] = remove_min(l2, x2, r2)
                    return bal(s1, m, s3)
                }
            }
        }
    }
}

export function remove<A>(x: A, t: Tree<A>, cmp: (_: A, __: A) => number): Tree<A> {
    switch (t.type) {
        case 'Empty': {
            return { type: 'Empty' }
        }
        case 'Node2': {
            const { left: l, value: y, right: r } = t
            switch (check(cmp(x, y)).type) {
                case 'Eq': {
                    return merge(l, r)
                }
                case 'Lt': {
                    return bal(remove(x, l, cmp), y, r)
                }
                case 'Gt': {
                    return bal(l, y, remove(x, r, cmp))
                }
            }
        }
    }
}

export function toList<A>(t: Tree<A>): A[] {
    switch (t.type) {
        case 'Empty': {
            return []
        }
        case 'Node2': {
            const { left: l, value: y, right: r } = t
            return [...toList(l), y, ...toList(r)]
        }
    }
}

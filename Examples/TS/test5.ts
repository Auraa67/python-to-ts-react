export type Tree<A, B> = Leaf<A, B> | LNode<A, B>

export interface Leaf<A, B> {
    type: 'Leaf'
    value: A
}

export interface LNode<A, B> {
    type: 'LNode'
    value: B
    left: Tree<A, B>
    right: Tree<A, B>
}

export function max(x: number, y: number): number {
    if (x > y) {
        return x
    } else {
        return y
    }
}

export function size(t: Tree<number, boolean>): number {
    switch (t.type) {
        case 'Leaf': {
            return 1
        }
        case 'LNode': {
            const { value: x, left: l, right: r } = t
            return max(size(l), size(r))
        }
        default: {
            return 1
        }
    }
}

export function length<A>(l: A[]): number {
    if (l.length > 0) {
        const [h, ...t] = l
        return 1 + length(t)
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

export function first<A, B>(z: [A, B]): A {
    const [x, y] = z
    return x
}

export function f5<A, B, C>(f: (_: A) => B, g: (_: B) => C): (_: A) => C {
    return x => g(f(x))
}

export function combine<A, B>(l1: A[], l2: B[]): [A, B][] {
    if (l1.length > 0) {
        const [h1, ...t1] = l1
        if (l2.length > 0) {
            const [h2, ...t2] = l2
            return [[h1, h2], ...combine(t1, t2)]
        } else {
            return []
        }
    } else {
        return []
    }
}

export function split<A, B>(l: [A, B][]): [A[], B[]] {
    if (l.length > 0) {
        const [h, ...t] = l
        const [l1, l2] = split(t)
        const [h1, h2] = h
        return [[h1, ...l1], [h2, ...l2]]
    } else {
        return [[], []]
    }
}
const l2 = [1, 3, 5, 7]
const l3 = [[2, 1], [7, 2]]
const l4: [string, number][] = [["e", 1], ["kjh", 2]]
const l: number[] = []

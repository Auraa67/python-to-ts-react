import { string_of_int } from './test14.ts'


type Tree<A> = Leaf<A> | LNode<A>

interface Leaf<A> {
    type: 'Leaf'
    value: A
}

interface LNode<A> {
    type: 'LNode'
    left: Tree<A>
    right: Tree<A>
}

type Tree2<A, B> = Leaf<A> | Node2<A, B>

interface Node2<A, B> {
    type: 'Node2'
    left: Tree2<A, B>
    right: Tree2<A, B>
}

function size<A>(t: Tree<A>): number {
    switch (t.type) {
        case 'Leaf': {
            return 1
        }
        case 'LNode': {
            const { left: l, right: r } = t
            return size(l) + size(r)
        }
    }
}

function length<A>(l: A[]): number {
    if (l.length > 0) {
        const [, ...t] = l
        return 1 + length(t)
    } else {
        return 0
    }
}

function is_empty<A>(l: A[]): boolean {
    if (l.length > 0) {
        return false
    } else {
        return true
    }
}

function hd<A>(l: A[]): A {
    if (l.length > 0) {
        const [h, ...t] = l
        return h
    } else {
        throw new Error()
    }
}

function tl<A>(l: A[]): A[] {
    if (l.length > 0) {
        const [h, ...t] = l
        return t
    } else {
        throw new Error()
    }
}

function join(l: string[], delim: string): string {
    if (l.length > 0) {
        const [h, ...t] = l
        if (is_empty(t)) {
            return h
        } else {
            return (h + delim) + join(t, delim)
        }
    } else {
        return ""
    }
}

function concat<A>(l1: A[], l2: A[]): A[] {
    if (l1.length > 0) {
        const [h1, ...t1] = l1
        return [h1, ...concat(t1, l2)]
    } else {
        return l2
    }
}

function to_list<A>(t: Tree<A>): A[] {
    switch (t.type) {
        case 'Leaf': {
            const { value: v } = t
            return [v]
        }
        case 'LNode': {
            const { left: l, right: r } = t
            return [...to_list(l), ...to_list(r)]
        }
    }
}

function reverse<A>(l: A[]): A[] {
    if (l.length > 0) {
        const [h, ...t] = l
        return [...reverse(t), h]
    } else {
        return []
    }
}

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

function map<A, B>(f: (_: A) => B, l: A[]): B[] {
    if (l.length > 0) {
        const [hd, ...tl] = l
        return [f(hd), ...map(f, tl)]
    } else {
        return []
    }
}

function fold_left<A, B>(f: (_: A, __: B) => A, init: A, l: B[]): A {
    if (l.length > 0) {
        const [h, ...t] = l
        return fold_left(f, f(init, h), t)
    } else {
        return init
    }
}
const l = { type: 'Leaf', value: 17 }
const t = { type: 'LNode', left: { type: 'Leaf', value: 5 }, right: { type: 'LNode', left: { type: 'Leaf', value: 3 }, right: { type: 'Leaf', value: 7 } } }
const lst = [21, 43, 56]
const s = length(lst)
const l3: [number, number][] = [[21, 43], [56, 78]]
const s42 = string_of_int(42)

console.log(s42)

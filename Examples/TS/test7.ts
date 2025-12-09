export type MyList<A> = MyNil<A> | MyCons<A>

export interface MyNil<A> {
    type: 'MyNil'
}

export interface MyCons<A> {
    type: 'MyCons'
    hd: A
    tl: MyList<A>
}

export type Colour = Red | Black | White

export interface Red {
    type: 'Red'
}

export interface Black {
    type: 'Black'
}

export interface White {
    type: 'White'
}

export type Tree<A, B> = Leaf<A, B> | Node2<A, B>

export interface Leaf<A, B> {
    type: 'Leaf'
    value: A
}

export interface Node2<A, B> {
    type: 'Node2'
    value: B
    left: Tree<A, B>
    right: Tree<A, B>
}

export interface Point {
    type: 'Point'
    x: number
    y: number
}

export interface Pair<A, B> {
    type: 'Pair'
    fst: A
    snd: B
}
const p: Pair<number, string> = { type: 'Pair', fst: 4, snd: "something" }
const p1 = p.fst
const p2 = p.snd

export function a(): number {
    switch (p.type) {
        case 'Pair': {
            const { fst: f, snd: s } = p
            return f
        }
    }
}

export function b(): string {
    switch (p.type) {
        case 'Pair': {
            const { fst: f, snd: s } = p
            return s
        }
    }
}

export function toInt(c: Colour): number {
    switch (c.type) {
        case 'Red': {
            return 0
        }
        case 'Black': {
            return 1
        }
        case 'White': {
            return 2
        }
    }
}

export function length<A>(l: MyList<A>): number {
    switch (l.type) {
        case 'MyNil': {
            return 0
        }
        case 'MyCons': {
            const { hd: h, tl: t } = l
            return 1 + length(t)
        }
    }
}

export function max(x: number, y: number): number {
    if (x > y) {
        return x
    } else {
        return y
    }
}

export function size<A, B>(t: Tree<A, B>): number {
    switch (t.type) {
        case 'Leaf': {
            return 1
        }
        case 'Node2': {
            const { left: l, right: r } = t
            return max(size(l), size(r))
        }
    }
}

export function copy(t: Tree<number, string>): Tree<number, string> {
    switch (t.type) {
        case 'Leaf': {
            const { value: a } = t
            return { type: 'Leaf', value: a }
        }
        case 'Node2': {
            const { value: b, left: l, right: r } = t
            const l2 = copy(l)
            const r2 = copy(r)
            return { type: 'Node2', value: b, left: l2, right: r2 }
        }
    }
}
const c: Colour = { type: 'Red' }
const l: Tree<number, string> = { type: 'Leaf', value: 3 }
const t: Tree<number, string> = { type: 'Node2', value: "abc", left: { type: 'Leaf', value: 7 }, right: { type: 'Leaf', value: size(l) } }

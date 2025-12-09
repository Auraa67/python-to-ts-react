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

export type Tree<A, C> = Leaf<A, C> | LNode<A, C>

export interface Leaf<A, C> {
    type: 'Leaf'
    value: A
}

export interface LNode<A, C> {
    type: 'LNode'
    value: C
    left: Tree<A, C>
    right: Tree<A, C>
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
            const { tl: t } = l
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
        case 'LNode': {
            const { left: l, right: r } = t
            return max(size(l), size(r))
        }
    }
}
const c = { type: 'Red' }
const l: Tree<number, string> = { type: 'Leaf', value: 3 }
const t = { type: 'LNode', value: "abc", left: { type: 'Leaf', value: 7 }, right: { type: 'Leaf', value: size(l) } }

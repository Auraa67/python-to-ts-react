export type Tree<A, B> = Leaf<A> | LNode<A, B>

export interface Leaf<A> {
    type: 'Leaf'
    value: A
}

export interface LNode<A, B> {
    type: 'LNode'
    value: B
    left: Tree<A, B>
    right: Tree<A, B>
}

export function mkLeaf<A>(value: A): Leaf<A> {
    return { type: 'Leaf', value: value }
}

export function mkLNode<A, B>(value: B, left: Tree<A, B>, right: Tree<A, B>): LNode<A, B> {
    return { type: 'LNode', value: value, left: left, right: right }
}

export function max(x: number, y: number): number {
    if (x > y) {
        return x
    } else {
        return y
    }
}

export function size(t: Tree<number, string>): number {
    switch (t.type) {
        case 'Leaf': {
            return 1
        }
        case 'LNode': {
            const { left: l, right: r } = t
            return 1 + max(size(l), size(r))
        }
    }
}
const t: Tree<number, string> = mkLNode("ok", mkLeaf(3), mkLeaf(5))
const s = size(t)

export type Tree<A> = Empty<A> | LNode<A>

export interface Empty<A> {
    type: 'Empty'
}

export interface LNode<A> {
    type: 'LNode'
    left: Tree<A>
    right: Tree<A>
}

export type int_Tree = Tree<number>

export type int_list = number[]

export type int_bool_tuple = [number, boolean]

export type nothing = undefined

export type call = (_: number, __: boolean) => string
const x = 3
const y: number = 9
const [a, b] = [(x + (y * 7)) - 10, 9]
const d = [1, 2, 3, 4]
const e = [1, 2, 3, 4]
const c = [...e]
const em: Tree<number> = { type: 'Empty' }
const no: Tree<number> = { type: 'LNode', left: { type: 'Empty' }, right: { type: 'Empty' } }

export function f(x: number): string {
    return x.toString()
}

export function size<A>(t: Tree<A>): number {
    switch (t.type) {
        case 'Empty': {
            return 0
        }
        case 'LNode': {
            const { right: r } = t
            return 1
        }
    }
}

export function head(l: number[]): number {
    if (l.length > 0) {
        const [h, ...t] = l
        return h
    } else {
        return 0
    }
}

export function times(x: number, y: number): number {
    if (x == 0) {
        return 0
    } else {
        return x * y
    }
}

export function handle(x: number, y: string): string {
    try {
        throw new RangeError()
    } catch (err) {
        if (err instanceof Error) {
            return y
        }
        throw err
    }
}

export function is_empty<A>(l: A[]): boolean {
    if (l.length > 0) {
        return true
    } else {
        return false
    }
}

export function concat<A>(l1: A[], l2: A[]): A[] {
    if (l1.length > 0) {
        const [h1, ...t1] = l1
        return [h1, ...concat(t1, l2)]
    } else {
        return l2
    }
}

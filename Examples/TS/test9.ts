type Tree<A, B> = Leaf<A, B> | LNode<A, B>

interface Leaf<A, B> {
    type: 'Leaf'
    value: A
}

interface LNode<A, B> {
    type: 'LNode'
    value: B
    left: Tree<A, B>
    right: Tree<A, B>
}

function max(x: number, y: number): number {
    if (x > y) {
        return x
    } else {
        return y
    }
}

function first<A, B>(z: [A, B]): A {
    const [x, ] = z
    return x
}

function size(t: Tree<number, string>): number {
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

function simple(t: Tree<number, string>): boolean {
    switch (t.type) {
        case 'Leaf': {
            return true
        }
        default: {
            return false
        }
    }
}

function compose<A, B, C>(f: (_: A) => B, g: (_: B) => C): (_: A) => C {
    return x => g(f(x))
}

function succ(x: number): number {
    return x + 1
}

function string_of_int(x: number): string {
    return x.toString()
}
const f = compose(succ, string_of_int)
const l: Tree<number, string> = { type: 'Leaf', value: 2 }
const t: Tree<number, string> = { type: 'LNode', value: "ok", left: { type: 'Leaf', value: 3 }, right: { type: 'Leaf', value: 5 } }

console.log(size(t))

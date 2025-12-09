import { type Tree, type LNode, type Leaf } from './trees.ts'
import * as trees from './trees.ts'

const t: Tree<number, string> = { type: 'LNode', value: "ok", left: { type: 'Leaf', value: 3 }, right: { type: 'Leaf', value: 5 } }

function size2(t: Tree<number, string>): number {
    return trees.size(t)
}

console.log(size2(t))

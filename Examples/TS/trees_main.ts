import { Tree, LNode, Leaf } from "./trees";
import * as trees from "./trees";
const t: Tree<number, string> = { kind: "LNode", value: { value: "ok", left: { kind: "Leaf", value: { value: 3 } }, right: { kind: "Leaf", value: { value: 5 } } } }
function size2(t: Tree<number, string>): number {
    return trees.size(t);
}

console.log(size2(t))

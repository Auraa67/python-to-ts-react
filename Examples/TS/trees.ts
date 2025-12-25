import { dataclass } from "./dataclasses";
type Tree<A, B> = Leaf<A> | LNode<A, B>;
interface Leaf<A> {
    value: A;
}
interface LNode<A, B> {
    value: B;
    left: Tree<A, B>;
    right: Tree<A, B>;
}
function mkLeaf<A>(value: A): Leaf<A> {
    return { kind: "Leaf", value: { value: value } };
}
function mkLNode<A, B>(value: B, left: Tree<A, B>, right: Tree<A, B>): LNode<A, B> {
    return { kind: "LNode", value: { value: value, left: left, right: right } };
}
function max(x: number, y: number): number {
    if (x > y) {
        return x;
    } else {
        return y;
    }
}
function size(t: Tree<number, string>): number {
    if (t.kind === "Leaf") {
        const value: _ = t.value;
        
        return 1;
    } else if (t.kind === "LNode") {
        const value: _, left: l, right: r = t.value;
        
        return (1 + max(size(l), size(r)));
    }
}
const t: Tree<number, string> = mkLNode("ok", mkLeaf(3), mkLeaf(5))
const s = size(t)

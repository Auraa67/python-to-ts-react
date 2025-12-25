import { Callable } from "./collections.abc";
import { dataclass } from "./dataclasses";
type Tree<A, B> = Leaf<A, B> | LNode<A, B>;
interface Leaf<A, B> {
    value: A;
}
interface LNode<A, B> {
    value: B;
    left: Tree<A, B>;
    right: Tree<A, B>;
}
function max(x: number, y: number): number {
    if (x > y) {
        return x;
    } else {
        return y;
    }
}
function first<A, B>(z: [A, B]): A {
    let x=z, _=z;
    return x;
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
function simple(t: Tree<number, string>): boolean {
    if (t.kind === "Leaf") {
        const value: _ = t.value;
        
        return true;
    } else if (t.kind === "_") {
        const  = t.value;
        
        return false;
    }
}
function compose<A, B, C>(f: (arg0: A) => B, g: (arg0: B) => C): (arg0: A) => C {
    return ((x) => g(f(x)));
}
function succ(x: number): number {
    return (x + 1);
}
function string_of_int(x: number): string {
    return str(x);
}
const f = compose(succ, string_of_int)
const l: Tree<number, string> = { kind: "Leaf", value: { value: 2 } }
const t: Tree<number, string> = { kind: "LNode", value: { value: "ok", left: { kind: "Leaf", value: { value: 3 } }, right: { kind: "Leaf", value: { value: 5 } } } }

print(size(t))

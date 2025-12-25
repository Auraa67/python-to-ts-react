import { string_of_int } from "./test14";
type Tree<A> = Leaf<A> | LNode<A>;
interface Leaf<A> {
    value: A;
}
interface LNode<A> {
    left: Tree<A>;
    right: Tree<A>;
}
type Tree2<A, B> = Leaf<A> | Node2<A, B>;
interface Node2<A, B> {
    left: Tree2<A, B>;
    right: Tree2<A, B>;
}
function size<A>(t: Tree<A>): number {
    if (t.kind === "Leaf") {
        return 1;
    } else if (t.kind === "LNode") {
        const { left: l, right: r } = t.value;
        return (size(l) + size(r));
    }
}
function length<A>(l: A[]): number {
    if (l.length === 0) {
        return 0;
    } else {
        const t= l.slice(1);
        return (1 + length(t));
    }
}
function is_empty<A>(l: A[]): boolean {
    if (l.length === 0) {
        return true;
    } else {
        return false;
    }
}
function hd<A>(l: A[]): A {
    if (l.length === 0) {
        throw new ValueError();
    } else {
        const h= l[0];
        const t= l.slice(1);
        return h;
    }
}
function tl<A>(l: A[]): A[] {
    if (l.length === 0) {
        throw new ValueError();
    } else {
        const h= l[0];
        const t= l.slice(1);
        return t;
    }
}
function join(l: string[], delim: string): string {
    if (l.length === 0) {
        return "";
    } else {
        const h= l[0];
        const t= l.slice(1);
        if (is_empty(t)) {
            return h;
        } else {
            return ((h + delim) + join(t, delim));
        }
    }
}
function concat<A>(l1: A[], l2: A[]): A[] {
    if (l1.length === 0) {
        return l2;
    } else {
        const h1= l1[0];
        const t1= l1.slice(1);
        return [h1, ...concat(t1, l2)];
    }
}
function to_list<A>(t: Tree<A>): A[] {
    if (t.kind === "Leaf") {
        const { value: v } = t.value;
        return [v];
    } else if (t.kind === "LNode") {
        const { left: l, right: r } = t.value;
        return [...to_list(l), ...to_list(r)];
    }
}
function reverse<A>(l: A[]): A[] {
    if (l.length === 0) {
        return [];
    } else {
        const h= l[0];
        const t= l.slice(1);
        return [...reverse(t), h];
    }
}
function unzip<A, B>(l: [A, B][]): [A[], B[]] {
    if (l.length === 0) {
        return [[], []];
    } else {
        const h= l[0];
        const t= l.slice(1);
        let [h1, h2] = h;
        let [t1, t2] = unzip(t);
        return [[h1, ...t1], [h2, ...t2]];
    }
}
function map<A, B>(f: (arg0: A) => B, l: A[]): B[] {
    if (l.length === 0) {
        return [];
    } else {
        const hd= l[0];
        const tl= l.slice(1);
        return [f(hd), ...map(f, tl)];
    }
}
function fold_left<A, B>(f: (arg0: A, arg1: B) => A, init: A, l: B[]): A {
    if (l.length === 0) {
        return init;
    } else {
        const h= l[0];
        const t= l.slice(1);
        return fold_left(f, f(init, h), t);
    }
}
const l = { kind: "Leaf", value: { value: 17 } }
const t = { kind: "LNode", value: { left: { kind: "Leaf", value: { value: 5 } }, right: { kind: "LNode", value: { left: { kind: "Leaf", value: { value: 3 } }, right: { kind: "Leaf", value: { value: 7 } } } } } }
const lst = [21, 43, 56]
const s = length(lst)
const l3: [number, number][] = [[21, 43], [56, 78]]
const s42 = string_of_int(42)

console.log(s42)

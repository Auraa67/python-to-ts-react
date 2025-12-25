import { dataclass } from "./dataclasses";
import { Callable } from "./collections.abc";
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
function size(t: Tree<number, boolean>): number {
    if (t.kind === "Leaf") {
        const value: _ = t.value;
        
        return 1;
    } else if (t.kind === "LNode") {
        const value: x, left: l, right: r = t.value;
        
        return max(size(l), size(r));
    } else if (t.kind === "_") {
        const  = t.value;
        
        return 1;
    }
}
function length<A>(l: A[]): number {
    if (l.length === 0) {
        return 0;
    } else {
        const h= l[0];
        const t= l.slice(1);
        return (1 + length(t));
    }
}
function concat<A>(l1: A[], l2: A[]): A[] {
    if (l1.length === 0) {
        return l2;
    } else {
        const h= l1[0];
        const t= l1.slice(1);
        return [h, ...concat(t, l2)];
    }
}
function first<A, B>(z: [A, B]): A {
    let x=z, y=z;
    return x;
}
function f5<A, B, C>(f: (arg0: A) => B, g: (arg0: B) => C): (arg0: A) => C {
    return ((x) => g(f(x)));
}
function combine<A, B>(l1: A[], l2: B[]): [A, B][] {
    if (l1.length === 0) {
        return [];
    } else {
        const h1= l1[0];
        const t1= l1.slice(1);
        if (l2.length === 0) {
            return [];
        } else {
            const h2= l2[0];
            const t2= l2.slice(1);
            return [[h1, h2], ...combine(t1, t2)];
        }
    }
}
function split<A, B>(l: [A, B][]): [A[], B[]] {
    if (l.length === 0) {
        return [[], []];
    } else {
        const h= l[0];
        const t= l.slice(1);
        let l1=split(t), l2=split(t);
        let h1=h, h2=h;
        return [[h1, ...l1], [h2, ...l2]];
    }
}
const l2 = [1, 3, 5, 7]
const l3 = [[2, 1], [7, 2]]
const l4: [string, number][] = [["e", 1], ["kjh", 2]]
const l: number[] = []

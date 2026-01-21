type MyList<A> = MyNil<A> | MyCons<A>;
interface MyNil<A> {
}
interface MyCons<A> {
    hd: A;
    tl: MyList<A>;
}
type Colour = Red | Black | White;
interface Red{
}
interface Black{
}
interface White{
}
type Tree<A, C> = Leaf<A, C> | LNode<A, C>;
interface Leaf<A, C> {
    value: A;
}
interface LNode<A, C> {
    value: C;
    left: Tree<A, C>;
    right: Tree<A, C>;
}
function toInt(c: Colour): number {
    if (c.kind === "Red") {
        const  = c.value;
        
        return 0;
    } else if (c.kind === "Black") {
        const  = c.value;
        
        return 1;
    } else if (c.kind === "White") {
        const  = c.value;
        
        return 2;
    }
}
function length<A>(l: MyList<A>): number {
    if (l.kind === "MyNil") {
        const  = l.value;
        
        return 0;
    } else if (l.kind === "MyCons") {
        const hd: _, tl: t = l.value;
        
        return (1 + length(t));
    }
}
function max(x: number, y: number): number {
    if (x > y) {
        return x;
    } else {
        return y;
    }
}
function size<A, B>(t: Tree<A, B>): number {
    if (t.kind === "Leaf") {
        const value: _ = t.value;
        
        return 1;
    } else if (t.kind === "LNode") {
        const value: _, left: l, right: r = t.value;
        
        return max(size(l), size(r));
    }
}
const c = { kind: "Red", value: {  } }
const l: Tree<number, string> = { kind: "Leaf", value: { value: 3 } }
const t = { kind: "LNode", value: { value: "abc", left: { kind: "Leaf", value: { value: 7 } }, right: { kind: "Leaf", value: { value: size(l) } } } }

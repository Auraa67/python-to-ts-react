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
type Tree<A, B> = Leaf<A, B> | Node2<A, B>;
interface Leaf<A, B> {
    value: A;
}
interface Node2<A, B> {
    value: B;
    left: Tree<A, B>;
    right: Tree<A, B>;
}
interface Point{
    x: number;
    y: number;
}
interface Pair<A, B> {
    fst: A;
    snd: B;
}
const p: Pair<number, string> = { kind: "Pair", value: { fst: 4, snd: "something" } }
const p1 = p.fst
const p2 = p.snd
function a(): number {
    if (p.kind === "Pair") {
        const fst: f, snd: s = p.value;
        
        return f;
    }
}
function b(): string {
    if (p.kind === "Pair") {
        const fst: f, snd: s = p.value;
        
        return s;
    }
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
        const hd: h, tl: t = l.value;
        
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
    } else if (t.kind === "Node2") {
        const value: _, left: l, right: r = t.value;
        
        return max(size(l), size(r));
    }
}
function copy(t: Tree<number, string>): Tree<number, string> {
    if (t.kind === "Leaf") {
        const value: a = t.value;
        
        return { kind: "Leaf", value: { value: a } };
    } else if (t.kind === "Node2") {
        const value: b, left: l, right: r = t.value;
        
        const l2 = copy(l)
        const r2 = copy(r)
        return { kind: "Node2", value: { value: b, left: l2, right: r2 } };
    }
}
const c: Colour = { kind: "Red", value: {  } }
const l: Tree<number, string> = { kind: "Leaf", value: { value: 3 } }
const t: Tree<number, string> = { kind: "Node2", value: { value: "abc", left: { kind: "Leaf", value: { value: 7 } }, right: { kind: "Leaf", value: { value: size(l) } } } }

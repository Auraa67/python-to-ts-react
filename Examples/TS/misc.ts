type Tree<A> = Empty<A> | LNode<A>;
interface Empty<A> {
}
interface LNode<A> {
    left: Tree<A>;
    right: Tree<A>;
}
type int_Tree = Tree<number>;
type int_list = number[];
type int_bool_tuple = [number, boolean];
type nothing = undefined;
type call = (arg0: number, arg1: boolean) => string;
const x = 3
const y: number = 9
let a=[((x + (y * 7)) - 10), 9], b=[((x + (y * 7)) - 10), 9];
const d = [1, 2, 3, 4]
const e = [1, 2, 3, 4]
const c = [...e]
const em: Tree<number> = { kind: "Empty", value: {  } }
const no: Tree<number> = { kind: "LNode", value: { left: { kind: "Empty", value: {  } }, right: { kind: "Empty", value: {  } } } }
function f(x: number): string {
    return x.toString();
}
function size<A>(t: Tree<A>): number {
    if (t.kind === "Empty") {
        const  = t.value;
        
        return 0;
    } else if (t.kind === "LNode") {
        const left: _, right: r = t.value;
        
        return 1;
    }
}
function head(l: number[]): number {
    if (l.length === 0) {
        return 0;
    } else {
        const h = l[0];
        const t = l.slice(1);
        return h;
    }
}
function times(x: number, y: number): number {
    if (x == 0) {
        return 0;
    } else {
        return (x * y);
    }
}
function handle(x: number, y: string): string {
    try {
        throw new IndexError();
    } catch (err) {
        if (err instanceof Exception) {
            return y;
        } else {
            throw err;
        }
    }
}
function is_empty<A>(l: A[]): boolean {
    if (l.length === 0) {
        return false;
    } else {
        const _ = l[0];
        const _ = l.slice(1);
        return true;
    }
}
function concat<A>(l1: A[], l2: A[]): A[] {
    if (l1.length === 0) {
        return l2;
    } else {
        const h1 = l1[0];
        const t1 = l1.slice(1);
        return [h1, ...concat(t1, l2)];
    }
}

type MyList<A> = Nil<A> | Cons<A>;
interface Nil<A> {
}
interface Cons<A> {
    hd: A;
    tl: MyList<A>;
}
function length<A>(l: MyList<A>): number {
    if (l.kind === "Nil") {
        return 0;
    } else if (l.kind === "Cons") {
        const { tl: t } = l.value;
        return (1 + length(t));
    }
}
function to_list<A>(l: MyList<A>): A[] {
    if (l.kind === "Nil") {
        return [];
    } else if (l.kind === "Cons") {
        const { hd: h, tl: t } = l.value;
        return [h, ...to_list(t)];
    }
}
function from_list<A>(l: A[]): MyList<A> {
    if (l.length === 0) {
        return { kind: "Nil", value: {  } };
    } else {
        const h= l[0];
        const t= l.slice(1);
        return { kind: "Cons", value: { hd: h, tl: from_list(t) } };
    }
}
const l = from_list(["a", "b", "c", "d", "e"])
const r = to_list(l)

console.log(r)

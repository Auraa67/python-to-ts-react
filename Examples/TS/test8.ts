import { Callable } from "./collections.abc";
function map<A, B>(f: (arg0: A) => B, l: A[]): B[] {
    function map2(acc: B[], l: A[]): B[] {
        if (l.length === 0) {
            return acc;
        } else {
            const hd= l[0];
            const tl= l.slice(1);
            return map2([f(hd), ...acc], tl);
        }
    }
    return map2([], l);
}

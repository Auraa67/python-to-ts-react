import { Callable } from "./collections.abc";
function f(x: number, y: number): (arg0: number) => number {
    return ((z) => (z * (x + y)));
}

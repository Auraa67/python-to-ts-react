import { Callable } from "./collections.abc";
function compose<A, B, C>(f: (arg0: A) => B, g: (arg0: B) => C): (arg0: A) => C {
    return ((x) => g(f(x)));
}

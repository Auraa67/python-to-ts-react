export function compose<A, B, C>(f: (_: A) => B, g: (_: B) => C): (_: A) => C {
    return x => g(f(x))
}

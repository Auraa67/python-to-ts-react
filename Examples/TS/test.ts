export function f1(x: number): number {
    return x * 2
}

export function f2(x: number, y: number): number {
    if (x < y) {
        return x
    } else {
        return y
    }
}

export function f3(x: number): (_: number) => number {
    return y => (y + x)
}

export function f4(f: (_: number) => boolean, g: (_: boolean) => string): (_: number) => string {
    return x => g(f(x))
}

export function f5<A, B, C>(f: (_: A) => B, g: (_: B) => C): (_: A) => C {
    return x => g(f(x))
}

export function f(x: number, y: number): (_: number) => number {
    return z => (z * (x + y))
}

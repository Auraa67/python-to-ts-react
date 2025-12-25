function f1(x: number): number {
    return (x * 2);
}
function f2(x: number, y: number): number {
    if (x < y) {
        return x;
    } else {
        return y;
    }
}
function f3(x: number): (arg0: number) => number {
    return ((y) => (y + x));
}
function f4(f: (arg0: number) => boolean, g: (arg0: boolean) => string): (arg0: number) => string {
    return ((x) => g(f(x)));
}
function f5<A, B, C>(f: (arg0: A) => B, g: (arg0: B) => C): (arg0: A) => C {
    return ((x) => g(f(x)));
}

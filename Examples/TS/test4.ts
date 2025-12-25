function empty<A>(l: A[]): boolean {
    if (l.length === 0) {
        return true;
    } else {
        return false;
    }
}
const l = [1, ...[2, ...[3, ...[]]]]

console.log(empty(l))

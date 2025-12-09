function empty<A>(l: A[]): boolean {
    if (l.length > 0) {
        return false
    } else {
        return true
    }
}
const l = [1, ...[2, ...[3, ...[]]]]

console.log(empty(l))

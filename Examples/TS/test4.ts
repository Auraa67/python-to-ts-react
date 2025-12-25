function empty<A>(l: A[]): boolean {
    if (l.length === 0) {
        return true;
    } else {
        const _= l[0];
        const _= l.slice(1);
        return false;
    }
}
const l = [1, ...[2, ...[3, ...[]]]]

print(empty(l))

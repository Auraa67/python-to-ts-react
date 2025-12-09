function insert<A>(l: A[], index: number, elt: A): A[] {
    if ((index < 0) || (index >= len(l))) {
        throw new RangeError()
    } else {
        return [...l.slice(0, index), elt, ...l.slice(index)]
    }
}

function update<A>(l: A[], index: number, elt: A): A[] {
    if ((index < 0) || (index > len(l))) {
        throw new RangeError()
    } else {
        return [...l.slice(0, index), elt, ...l.slice(index + 1)]
    }
}
const l = [1, 2, 3, 4, 5]

console.log(insert(l, 3, 9))

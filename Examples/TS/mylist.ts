type MyList<A> = Nil<A> | Cons<A>

interface Nil<A> {
    type: 'Nil'
}

interface Cons<A> {
    type: 'Cons'
    hd: A
    tl: MyList<A>
}

function length<A>(l: MyList<A>): number {
    switch (l.type) {
        case 'Nil': {
            return 0
        }
        case 'Cons': {
            const { tl: t } = l
            return 1 + length(t)
        }
    }
}

function to_list<A>(l: MyList<A>): A[] {
    switch (l.type) {
        case 'Nil': {
            return []
        }
        case 'Cons': {
            const { hd: h, tl: t } = l
            return [h, ...to_list(t)]
        }
    }
}

function from_list<A>(l: A[]): MyList<A> {
    if (l.length > 0) {
        const [h, ...t] = l
        return { type: 'Cons', hd: h, tl: from_list(t) }
    } else {
        return { type: 'Nil' }
    }
}
const l = from_list(["a", "b", "c", "d", "e"])
const r = to_list(l)

console.log(r)

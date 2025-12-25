type Comparaison= Eq | Lt | Gt;
interface Eq{
}
interface Lt{
}
interface Gt{
}
type Tree<A> = Empty<A> | Node2<A>;
interface Empty<A> {
}
interface Node2<A> {
    height: number;
    left: Tree<A>;
    value: A;
    right: Tree<A>;
}
function check(res: number): Comparaison {
    if (res == 0) {
        return { kind: "Eq", value: {  } };
    } else {
        if (res < 0) {
            return { kind: "Lt", value: {  } };
        } else {
            return { kind: "Gt", value: {  } };
        }
    }
}
function max(i: number, j: number): number {
    if (i > j) {
        return i;
    } else {
        return j;
    }
}
function get_or_else<A>(v: A | undefined, other: A): A {
    if (v === undefined) {
        return other;
    } else {
        return v;
    }
}
function is_empty<A>(t: Tree<A>): boolean {
    if (t.kind === "Empty") {
        return true;
    } else if (t.kind === "_") {
        return false;
    }
}
function mem<A>(x: A, t: Tree<A>, cmp: (arg0: A, arg1: A) => number): boolean {
    if (t.kind === "Empty") {
        return false;
    } else if (t.kind === "Node2") {
        const { left: l, value: k, right: r } = t.value;
        if (check(cmp(x, k)).kind === "Eq") {
            return true;
        } else if (check(cmp(x, k)).kind === "Lt") {
            return mem(x, l, cmp);
        } else if (check(cmp(x, k)).kind === "Gt") {
            return mem(x, r, cmp);
        }
    }
}
function find<A>(x: A, t: Tree<A>, cmp: (arg0: A, arg1: A) => number): A | undefined {
    if (t.kind === "Empty") {
        return undefined;
    } else if (t.kind === "Node2") {
        const { left: l, value: k, right: r } = t.value;
        if (check(cmp(x, k)).kind === "Eq") {
            return k;
        } else if (check(cmp(x, k)).kind === "Lt") {
            return find(x, l, cmp);
        } else if (check(cmp(x, k)).kind === "Gt") {
            return find(x, r, cmp);
        }
    }
}
function min_elt<A>(t: Tree<A>): A | undefined {
    if (t.kind === "Empty") {
        return undefined;
    } else if (t.kind === "Node2") {
        const { left: l, value: x } = t.value;
        if (l.kind === "Empty") {
            return x;
        } else if (l.kind === "Node2") {
            return min_elt(l);
        }
    }
}
function max_elt<A>(t: Tree<A>): A | undefined {
    if (t.kind === "Empty") {
        return undefined;
    } else if (t.kind === "Node2") {
        const { value: x, right: r } = t.value;
        if (r.kind === "Empty") {
            return x;
        } else if (r.kind === "Node2") {
            return max_elt(r);
        }
    }
}
function height<A>(t: Tree<A>): number {
    if (t.kind === "Empty") {
        return 0;
    } else if (t.kind === "Node2") {
        const { height: h } = t.value;
        return h;
    }
}
function size<A>(t: Tree<A>): number {
    if (t.kind === "Empty") {
        return 0;
    } else if (t.kind === "Node2") {
        const { left: l, right: r } = t.value;
        return ((size(l) + size(r)) + 1);
    }
}
function create<A>(l: Tree<A>, x: A, r: Tree<A>): Tree<A> {
    const hl: number = height(l)
    const hr: number = height(r)
    return { kind: "Node2", value: { height: (max(hl, hr) + 1), left: l, value: x, right: r } };
}
function leaf<A>(x: A): Tree<A> {
    return create({ kind: "Empty", value: {  } }, x, { kind: "Empty", value: {  } });
}
function bal<A>(l: Tree<A>, x: A, r: Tree<A>): Tree<A> {
    const hl: number = height(l)
    const hr: number = height(r)
    if ((hr + 2) < hl) {
        if (l.kind === "Empty") {
            throw new SystemExit();
        } else if (l.kind === "Node2") {
            const { left: ll, value: lx, right: lr } = l.value;
            if (!(height(lr) > height(ll))) {
                const rs = create(lr, x, r)
                return create(ll, lx, rs);
            } else {
                if (lr.kind === "Empty") {
                    throw new SystemExit();
                } else if (lr.kind === "Node2") {
                    const { left: lrl, value: lrx, right: lrr } = lr.value;
                    const ls = create(ll, lx, lrl)
                    const rs = create(lrr, x, r)
                    return create(ls, lrx, rs);
                }
            }
        }
    } else {
        if ((hl + 2) < hr) {
            if (r.kind === "Empty") {
                throw new SystemExit();
            } else if (r.kind === "Node2") {
                const { left: rl, value: rx, right: rr } = r.value;
                if (!(height(rl) > height(rr))) {
                    const ls = create(l, x, rl)
                    return create(ls, rx, rr);
                } else {
                    if (rl.kind === "Empty") {
                        throw new SystemExit();
                    } else if (rl.kind === "Node2") {
                        const { left: rll, value: rlx, right: rlr } = rl.value;
                        const ls = create(l, x, rll)
                        const rs = create(rlr, rx, rr)
                        return create(ls, rlx, rs);
                    }
                }
            }
        } else {
            return create(l, x, r);
        }
    }
}
function add<A>(x: A, t: Tree<A>, cmp: (arg0: A, arg1: A) => number): Tree<A> {
    if (t.kind === "Empty") {
        return leaf(x);
    } else if (t.kind === "Node2") {
        const { left: l, value: y, right: r } = t.value;
        if (check(cmp(x, y)).kind === "Eq") {
            return create(l, y, r);
        } else if (check(cmp(x, y)).kind === "Lt") {
            return bal(add(x, l, cmp), y, r);
        } else if (check(cmp(x, y)).kind === "Gt") {
            return bal(l, y, add(x, r, cmp));
        }
    }
}
function remove_min<A>(l: Tree<A>, x: A, r: Tree<A>): [Tree<A>, A] {
    if (l.kind === "Empty") {
        return [r, x];
    } else if (l.kind === "Node2") {
        const { left: ll, value: lx, right: lr } = l.value;
        let [l2, m] = remove_min(ll, lx, lr);
        return [bal(l2, x, r), m];
    }
}
function merge<A>(s1: Tree<A>, s2: Tree<A>): Tree<A> {
    if (s1.kind === "Empty") {
        return s2;
    } else if (s1.kind === "Node2") {
        if (s2.kind === "Empty") {
            return s1;
        } else if (s2.kind === "Node2") {
            const { left: l2, value: x2, right: r2 } = s2.value;
            let [s3, m] = remove_min(l2, x2, r2);
            return bal(s1, m, s3);
        }
    }
}
function remove<A>(x: A, t: Tree<A>, cmp: (arg0: A, arg1: A) => number): Tree<A> {
    if (t.kind === "Empty") {
        return { kind: "Empty", value: {  } };
    } else if (t.kind === "Node2") {
        const { left: l, value: y, right: r } = t.value;
        if (check(cmp(x, y)).kind === "Eq") {
            return merge(l, r);
        } else if (check(cmp(x, y)).kind === "Lt") {
            return bal(remove(x, l, cmp), y, r);
        } else if (check(cmp(x, y)).kind === "Gt") {
            return bal(l, y, remove(x, r, cmp));
        }
    }
}
function toList<A>(t: Tree<A>): A[] {
    if (t.kind === "Empty") {
        return [];
    } else if (t.kind === "Node2") {
        const { left: l, value: y, right: r } = t.value;
        return [...toList(l), y, ...toList(r)];
    }
}

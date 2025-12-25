function unzip<A, B>(l: [A, B][]): [A[], B[]] {
    if (l.length === 0) {
        return [[], []];
    } else {
        const h= l[0];
        const t= l.slice(1);
        let h1=h, h2=h;
        let t1=unzip(t), t2=unzip(t);
        return [[h1, ...t1], [h2, ...t2]];
    }
}

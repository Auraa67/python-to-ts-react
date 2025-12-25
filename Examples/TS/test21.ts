interface Point{
    x: number;
    y: number;
}
const pt: Point = { kind: "Point", value: { x: 3, y: 5 } }
function init(z: number): Point {
    return { kind: "Point", value: { x: z, y: z } };
}
const pt2: Point = {...pt, y: 10}

console.log(pt2)

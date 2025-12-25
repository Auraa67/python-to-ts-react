interface Point{
    x: number;
    y: number;
}
const pt: Point = { kind: "Point", value: { x: 3, y: 5 } }
function init(z: number): Point {
    return { kind: "Point", value: { x: z, y: z } };
}

console.log(pt.y)

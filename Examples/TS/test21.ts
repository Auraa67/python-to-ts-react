interface Point {
    type: 'Point'
    x: number
    y: number
}
const pt: Point = { type: 'Point', x: 3, y: 5 }

function init(z: number): Point {
    return { type: 'Point', x: z, y: z }
}
const pt2: Point = { ...pt, y: 10 }

console.log(pt2)

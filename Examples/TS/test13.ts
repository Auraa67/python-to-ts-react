interface Point {
    type: 'Point'
    x: number
    y: number
}
const pt: Point = { type: 'Point', x: 3, y: 5 }

function init(z: number): Point {
    return { type: 'Point', x: z, y: z }
}

console.log(pt.y)

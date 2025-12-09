export function len<A>(seq: A[] | string): number {
    return seq.length
}

// Works only for serializable data types, see:
// https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON
export function equal<A>(e1: A, e2: A): boolean {
    return JSON.stringify(e1) === JSON.stringify(e2)
}
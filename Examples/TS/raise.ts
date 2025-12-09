function f(): string {
    throw new TypeError("error message")
}

function main(): string {
    try {
        return f()
    } catch (err) {
        if (err instanceof TypeError) {
            return "Type error: " + err.toString()
        }
        throw err
    }
}

console.log(main())

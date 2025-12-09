export interface Task {
    type: 'Task'
    id: number
    text: string
    done: boolean
}

export type State = Task[]

export type Action = Added | Changed | Deleted

export interface Added {
    type: 'Added'
    id: number
    text: string
}

export interface Changed {
    type: 'Changed'
    task: Task
}

export interface Deleted {
    type: 'Deleted'
    id: number
}

export function map<A, B>(f: (_: A) => B, l: A[]): B[] {
    if (l.length > 0) {
        const [h, ...t] = l
        return [f(h), ...map(f, t)]
    } else {
        return []
    }
}

export function filter<A>(f: (_: A) => boolean, l: A[]): A[] {
    if (l.length > 0) {
        const [h, ...t] = l
        if (f(h)) {
            return [h, ...filter(f, t)]
        } else {
            return filter(f, t)
        }
    } else {
        return []
    }
}

export function tasksReducer(tasks: State, action: Action): State {
    switch (action.type) {
        case 'Added': {
            const { id: id, text: text } = action
            return [...tasks, { type: 'Task', id: id, text: text, done: false }]
        }
        case 'Changed': {
            const { task: task } = action
            return map(t => ((t.id == task.id) ? task : t), tasks)
        }
        case 'Deleted': {
            const { id: id } = action
            return filter(t => (!(t.id == id)), tasks)
        }
    }
}

import { dataclass } from "./dataclasses";
import { Callable } from "./collections.abc";
interface Task{
    id: number;
    text: string;
    done: boolean;
}
type State= Task[];
type Action= Added | Changed | Deleted;
interface Added{
    id: number;
    text: string;
}
interface Changed{
    task: Task;
}
interface Deleted{
    id: number;
}
function map<A, B>(f: (arg0: A) => B, l: A[]): B[] {
    if (l.length === 0) {
        return [];
    } else {
        const h= l[0];
        const t= l.slice(1);
        return [f(h), ...map(f, t)];
    }
}
function filter<A>(f: (arg0: A) => boolean, l: A[]): A[] {
    if (l.length === 0) {
        return [];
    } else {
        const h= l[0];
        const t= l.slice(1);
        if (f(h)) {
            return [h, ...filter(f, t)];
        } else {
            return filter(f, t);
        }
    }
}
function tasksReducer(tasks: State, action: Action): State {
    if (action.kind === "Added") {
        const id: id, text: text = action.value;
        
        return [...tasks, { kind: "Task", value: { id: id, text: text, done: false } }];
    } else if (action.kind === "Changed") {
        const task: task = action.value;
        
        return map(((t) => ((t.id == task.id) ? task : t)), tasks);
    } else if (action.kind === "Deleted") {
        const id: id = action.value;
        
        return filter(((t) => (!(t.id == id))), tasks);
    }
}

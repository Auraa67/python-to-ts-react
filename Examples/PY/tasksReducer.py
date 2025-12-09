from dataclasses import dataclass
from collections.abc import Callable
@dataclass
class Task:
    id: int
    text: str
    done: bool
type State = list[Task]
type Action = Added | Changed | Deleted
@dataclass
class Added:
    id: int
    text: str
@dataclass
class Changed:
    task: Task
@dataclass
class Deleted:
    id: int
def map[A, B](f: Callable[[A], B], l: list[A]) -> list[B]:
    match l:
        case [h, *t]:
            return [f(h), *(map(f, t))]
        case _:
            return []
def filter[A](f: Callable[[A], bool], l: list[A]) -> list[A]:
    match l:
        case [h, *t]:
            if f(h):
                return [h, *(filter(f, t))]
            else:
                return filter(f, t)
        case _:
            return []
def tasksReducer(tasks: State, action: Action) -> State:
    match action:
        case Added(id=id, text=text):
            return [*tasks, Task(id=id, text=text, done=False)]
        case Changed(task=task):
            return map(lambda t: task if (t.id == task.id) else t, tasks)
        case Deleted(id=id):
            return filter(lambda t: not(t.id == id), tasks)

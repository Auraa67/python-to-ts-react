from dataclasses import dataclass

type Expr = Val | Add | Mul | Neg

@dataclass
class Val:
    i: int

@dataclass
class Add:
    left: Expr
    right: Expr

@dataclass
class Mul:
    left: Expr
    right: Expr

@dataclass
class Neg:
    e: Expr

def eval(e: Expr) -> int:
    match e:
        case Val(i=x):
            return x
        case Add(left=l, right=r):
            return eval(l) + eval(r)
        case Mul(left=l, right=r):
            return eval(l) * eval(r)
        case Neg(e=sub):
            return 0 - eval(sub)

expr = Add(
    left=Neg(e=Val(i=5)),
    right=Mul(left=Val(i=3), right=Val(i=4))
)
res = eval(expr)

print(res)
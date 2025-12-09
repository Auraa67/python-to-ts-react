from trees import Tree, LNode, Leaf
import trees
t: Tree[int, str] = LNode(value="ok", left=Leaf(value=3), right=Leaf(value=5))
def size2(t: Tree[int, str]) -> int:
    return trees.size(t)

print(size2(t))

@dataclass
class Node[T]:
    value: T
    left: Optional['Node[T]'] = None
    right: Optional['Node[T]'] = None
    
type BTree[T] = Node[T] | None

def preorder[T](tree: BTree[T]):
    match tree:
        case Node(value, left, right):
            print(value)
            preorder(left)
            preorder(right)
        case _:
            return
        
        
def postorder[T](tree: BTree[T]):
    match tree:
        case Node(value, left, right):
            postorder(left)
            postorder(right)
            print(value)
        case _:
            return
        
        
def inorder[T](tree: BTree[T]):
    match tree:
        case Node(value, left, right):
            inorder(left)
            print(value)
            inorder(right)
        case _:
            return
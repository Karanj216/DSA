class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    n = int(input("Enter data (0 to stop): "))
    if n == 0:
        return None

    root = Node(n)
    print(f"Enter left child of {n}:")
    root.left = create()
    print(f"Enter right child of {n}:")
    root.right = create()
    return root

# Preorder traversal
def preorder(node):
    if node is not None:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

# Inorder traversal
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

root = create()
print("\n Preorder Traversal:")
preorder(root)
print("\n Inorder Traversal:")
inorder(root)
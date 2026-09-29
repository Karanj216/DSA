class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    x = int(input("Enter the data (-1 for no node): "))

    if x == -1:
        return None

    root = Node(x)

    print(f"Enter left of {x}")
    root.left = create()

    print(f"Enter right of {x}")
    root.right = create()

    return root


class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [None] * 100

    def push(self, x):
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return None

        x = self.st[self.TOP]
        self.TOP -= 1
        return x


def preorder(root):
    s = Stack()

    while root is not None:
        print(root.data, end=" ")
        s.push(root)
        root = root.left

    while s.TOP != -1:
        r = s.pop()
        r = r.right

        while r is not None:
            print(r.data, end=" ")
            s.push(r)
            r = r.left


def inorder(root):
    s1 = Stack()

    while root is not None:
        s1.push(root)
        root = root.left

    while s1.TOP != -1:
        root = s1.pop()
        print(root.data, end=" ")

        root = root.right

        while root is not None:
            s1.push(root)
            root = root.left

def postorder(root):
    if root is None:
        return

    s1 = Stack()
    s2 = Stack()

    s1.push(root)

    while s1.TOP != -1:
        node = s1.pop()
        s2.push(node)

        if node.left is not None:
            s1.push(node.left)

        if node.right is not None:
            s1.push(node.right)

    while s2.TOP != -1:
        print(s2.pop().data, end=" ")

x = create()

print("\nPreorder:")
preorder(x)

print("\nInorder:")
inorder(x)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Library:
    def __init__(self):
        self.root = None

    # Recursive insertion
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root

    # Recursive inorder traversal
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Recursive preorder traversal
    def preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Recursive postorder traversal
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


# Create Library object
library = Library()

while True:
    print("\n===== LIBRARY CATALOG =====")
    print("1. Insert Book")
    print("2. Inorder Navigation")
    print("3. Preorder Navigation")
    print("4. Postorder Navigation")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        library.root = library.insert(library.root, book_id)
        print("Book inserted successfully.")

    elif choice == 2:
        print("Books in sorted order:")
        library.inorder(library.root)
        print()

    elif choice == 3:
        print("Preorder navigation:")
        library.preorder(library.root)
        print()

    elif choice == 4:
        print("Postorder navigation:")
        library.postorder(library.root)
        print()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
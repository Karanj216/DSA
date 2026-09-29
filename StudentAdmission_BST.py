class Node:
    def __init__(self, admission_no, name):
        self.admission_no = admission_no
        self.name = name
        self.left = None
        self.right = None


class StudentBST:
    def __init__(self):
        self.root = None

    # Recursive insertion
    def insert(self, root, admission_no, name):
        if root is None:
            return Node(admission_no, name)

        if admission_no < root.admission_no:
            root.left = self.insert(root.left, admission_no, name)

        elif admission_no > root.admission_no:
            root.right = self.insert(root.right, admission_no, name)

        else:
            print("Admission number already exists.")

        return root

    # Recursive inorder traversal
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.admission_no, "-", root.name)
            self.inorder(root.right)

    # Recursive search
    def search(self, root, admission_no):
        if root is None:
            return None

        if root.admission_no == admission_no:
            return root

        if admission_no < root.admission_no:
            return self.search(root.left, admission_no)

        return self.search(root.right, admission_no)


# Create BST
bst = StudentBST()

while True:
    print("\n===== STUDENT ADMISSION MANAGEMENT =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        admission_no = int(input("Enter Admission Number: "))
        name = input("Enter Student Name: ")

        bst.root = bst.insert(bst.root, admission_no, name)
        print("Student record added successfully.")

    elif choice == 2:
        if bst.root is None:
            print("No student records available.")
        else:
            print("\nStudent Records:")
            bst.inorder(bst.root)

    elif choice == 3:
        admission_no = int(input("Enter Admission Number to search: "))

        result = bst.search(bst.root, admission_no)

        if result is not None:
            print("Student Found!")
            print("Admission Number:", result.admission_no)
            print("Name:", result.name)
        else:
            print("Student not found.")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
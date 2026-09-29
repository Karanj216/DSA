class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        print("Book inserted at beginning.")

    # Insert at end
    def insert_end(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            print("Book inserted at end.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        print("Book inserted at end.")

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("Library catalog is empty.")
            return

        print("Deleted book:", self.head.data)
        self.head = self.head.next

    # Display
    def show(self):
        if self.head is None:
            print("Library catalog is empty.")
            return

        temp = self.head

        print("Library Catalog:")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Create linked list object
ll = LL()

while True:
    print("\n===== LIBRARY CATALOG =====")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter book ID: "))
        ll.insert_beginning(val)

    elif choice == 2:
        val = int(input("Enter book ID: "))
        ll.insert_end(val)

    elif choice == 3:
        ll.delete_beginning()

    elif choice == 4:
        ll.show()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
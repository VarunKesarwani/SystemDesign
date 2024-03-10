class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        print("Elements in the linked list are: ")
        while printval is not None:
            print(printval.dataval, end=" ")
            printval = printval.nextval
        print("\n")

    def delete_after_data(self, search_data):
        current = self.headval
        prev = Node()
        if current is None:
            return 0
        if current is not None:
            if current.dataval == search_data:
                self.headval = current.nextval
                current = None
                return 1
        while current is not None:
            if current.dataval == search_data:
                break
            prev = current
            current = current.nextval

        if current is None:
            return 0

        prev.nextval = current.nextval
        current = None
        return 1


if __name__ == "__main__":
    List = SLinkedList()
    first_data = input("Enter the first data of the Linked List: ")
    List.headval = Node(first_data)
    current_node = List.headval
    while 1:
        print("1. Enter 1 to insert in list.")
        print("2. Enter 2 to print the list.")
        print("3. Enter 3 to delete at the head.")
        print("4. Enter 4 to delete after specific node.")
        print("0. Enter 0 to exit.")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter the data you want in the list: ")
            new_node = Node(data)
            current_node.nextval = new_node
            current_node = new_node
        elif choice == 2:
            List.listprint()
        elif choice == 3:
            print("Delete data at the head.")
            new_node = List.headval
            List.headval = List.headval.nextval
            new_node = None
        elif choice == 4:
            search_data = input("After which element you want to delete: ")
            a = List.delete_after_data(search_data)
            if a == 1:
                print("Element Deleted.")
            else:
                print("Element not Deleted.")
        elif choice == 0:
            exit()

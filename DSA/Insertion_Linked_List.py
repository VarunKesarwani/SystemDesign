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

    def insert_after_data(self, search_data, data):
        current = self.headval
        if current is None:
            return 0
        while current is not None and current.dataval != search_data:
            current = current.nextval

        if current.dataval == search_data:
            new_node = Node(data)
            new_node.nextval = current.nextval
            current.nextval = new_node
            return 1
        else:
            return 0


if __name__ == "__main__":
    List = SLinkedList()
    first_data = input("Enter the first data of the Linked List: ")
    List.headval = Node(first_data)
    current_node = List.headval
    while 1:
        print("1. Enter 1 to insert in list.")
        print("2. Enter 2 to print the list.")
        print("3. Enter 3 to insert at the head.")
        print("4. Enter 4 to insert after specific node.")
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
            data = input("Enter the data you want in the list: ")
            new_node = Node(data)
            new_node.nextval = List.headval
            List.headval = new_node
        elif choice == 4:
            search_data = input("After which element you want to insert: ")
            data = input("Enter the data you want in the list: ")
            a = List.insert_after_data(search_data, data)
            if a == 1:
                print("Element Inserted.")
            else:
                print("Element not inserted.")
        elif choice == 0:
            exit()

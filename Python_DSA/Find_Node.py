class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        if self.headval is None:
            print("Linked list is empty.")
            return 0
        else:
            printval = self.headval
            print("Elements in the linked list are: ")
            while printval is not None:
                print(printval.dataval, end=" ")
                printval = printval.nextval
            print("\n")
            return 1

    def finding_node(self, search_data):
        current = self.headval
        while current is not None:
            if current.dataval == search_data:
                return 1
            current = current.nextval
        return -1


if __name__ == "__main__":
    List = SLinkedList()
    first_data = input("Enter the first data of the Linked List: ")
    List.headval = Node(first_data)
    current_node = List.headval
    while 1:
        print("1. Enter 1 to insert in list.")
        print("2. Enter 2 to print the list.")
        print("3. Enter 3 to Find the node in Linked List.")
        print("0. Enter 0 to exit.")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter the data you want in the list: ")
            new_node = Node(data)
            current_node.nextval = new_node
            current_node = new_node
        elif choice == 2:
            if List.listprint() == 0:
                first_data = input("Enter the first data of the Linked List: ")
                List.headval = Node(first_data)
                current_node = List.headval
        elif choice == 3:
            search_data = input("Enter the value you want to search. ")
            res = List.finding_node(search_data)
            if res == -1:
                print("Element is not present in Linked List.")
            else:
                print("Element found in the Linked List.")
        elif choice == 0:
            exit()

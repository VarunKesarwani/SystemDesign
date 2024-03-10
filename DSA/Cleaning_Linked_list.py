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

    def cleaning_list(self):
        self.__init__()


if __name__ == "__main__":
    List = SLinkedList()
    first_data = input("Enter the first data of the Linked List: ")
    List.headval = Node(first_data)
    current_node = List.headval
    while 1:
        print("1. Enter 1 to insert in list.")
        print("2. Enter 2 to print the list.")
        print("3. Enter 3 to delete the Linked List.")
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
            print("Cleaning the Linked List")
            List.cleaning_list()
        elif choice == 0:
            exit()

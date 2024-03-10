class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node

    def print_stack(self):
        curr = self.top
        if curr is None:
            print("Stack is empty. ")
        else:
            print("TOP")
            while curr is not None:
                print(curr.data)
                curr = curr.next

            print("BOTTOM")

    def isempty(self):
        if self.top is None:
            return True
        else:
            return False

    def peek(self):
        if self.isempty():
            return False
        else:
            print(self.top.data)
            return True


if __name__ == "__main__":
    a_stack = Stack()
    while True:
        print('1. push')
        print('2. print')
        print('3. Peek')
        print('0. quit')
        operation = int(input('What would you like to do? '))

        if operation == 1:
            push_data = int(input("Enter the number you want to push: "))
            a_stack.push(push_data)
        elif operation == 2:
            a_stack.print_stack()
        elif operation == 3:
            if a_stack.peek():
                print("This is the top element.")
            else:
                print("Stack is empty.")
        elif operation == 0:
            exit()

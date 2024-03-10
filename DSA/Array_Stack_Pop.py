class MyStack:
    def __init__(self):
        self.container = []  # You don't want to assign [] to self

    def push(self, item):
        self.container.append(item)  # appending to the *container*, not the instance itself.

    def isempty(self):
        return len(self.container) == 0

    def pop(self):
        if s.isempty():
            print("Stack is empty. Pop is not possible.")
        else:
            return self.container.pop()  # pop from the container

    def show(self):
        if s.isempty():
            print("Stack is empty. Nothing to show.")
            self.container
        else:
            return self.container  # display the entire stack as list


if __name__ == "__main__":
    s = MyStack()
    while 1:
        print("1. To push data")
        print("2. To show the stack.")
        print("3. To Pop from stack.")
        print("0. To exit")
        choice = int(input())
        if choice == 1:
            data = input("Enter the data you want to push?")
            s.push(data)
        if choice == 2:
            print(s.show())
        if choice == 3:
            s.pop()
        if choice == 0:
            exit()

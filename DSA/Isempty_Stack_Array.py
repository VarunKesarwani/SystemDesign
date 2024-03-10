class MyStack:
    def __init__(self):
        self.container = []  # You don't want to assign [] to self

    def isempty(self):
        return len(self.container) == 0  # While there's nothing wrong with self.container == []

    def push(self, item):
        self.container.append(item)  # appending to the *container*, not the instance itself.

    def show(self):
        return self.container  # display the entire stack as list


if __name__ == "__main__":
    s = MyStack()
    while 1:
        print("1. To push data")
        print("2. to show the stack.")
        print("3. To check if stack is empty.")
        print("0. To exit")
        choice = int(input())
        if choice == 1:
            data = input("Enter the data you want to push?")
            s.push(data)
        if choice == 2:
            print(s.show())
        if choice == 3:
            val = s.isempty()
            if val:
                print("Stack is empty.")
            else:
                print("Stack is not empty.")
        if choice == 0:
            exit()

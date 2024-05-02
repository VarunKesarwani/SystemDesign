class MyStack:
    def __init__(self):
        self.container = []  # You don't want to assign [] to self

    def push(self, item):
        self.container.append(item)

    def show(self):
        return self.container  # display the entire stack as list


if __name__ == "__main__":
    s = MyStack()
    while 1:
        print("1. To push data")
        print("2. to show the stack.")
        print("0. To exit")
        choice = int(input())
        if choice == 1:
            data = input("Enter the data you want to push?")
            s.push(data)
        if choice == 2:
            print(s.show())
        if choice == 0:
            exit()


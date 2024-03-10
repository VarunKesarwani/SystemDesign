class MyStack:
    def __init__(self):
        self.container = []  # You don't want to assign [] to self

    def push(self, item):
        self.container.append(item)


if __name__ == "__main__":
    s = MyStack()
    while 1:
        print("1. To push data")
        print("0. To exit")
        choice = int(input())
        if choice == 1:
            data = input("Enter the data you want to push?")
            s.push(data)
        if choice == 0:
            exit()
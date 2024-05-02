class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        tmp = Node(data)
        if self.rear is None:
            self.front = self.rear = tmp
            return
        else:
            self.rear.next = self.rear = tmp


if __name__ == "__main__":
    q = Queue()
    while True:
        print('1. enqueue')
        print('0. quit')
        operation = int(input('What would you like to do? '))
        if operation == 1:
            data = input("Enter element you want to insert: ")
            q.enqueue(data)
        elif operation == 0:
            exit()
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

    def show(self):
        if self.isempty():
            print("Queue is empty.")
        else:
            a = self.front
            print("FRONT")
            while a is not None:
                print(a.data)
                a = a.next
            print("REAR")

    def deque(self):
        if self.isempty() or self.front is None:
            print("Queue is empty")
            self.front = None
            self.rear = None
        else:
            print("Deleted element is element of Queue is :", end =" ")
            print(self.front.data)
            self.front = self.front.next

    def isempty(self):
        if self.rear is None:
            return True
        else:
            return False


if __name__ == "__main__":
    q = Queue()
    while True:
        print('1. enqueue')
        print('2. show')
        print('3. Delete element')
        print('0. quit')
        operation = int(input('What would you like to do? '))

        if operation == 1:
            data = input("Enter element you want to insert: ")
            q.enqueue(data)
        elif operation == 2:
            q.show()
        elif operation == 3:
            q.deque()
        elif operation == 0:
            exit()

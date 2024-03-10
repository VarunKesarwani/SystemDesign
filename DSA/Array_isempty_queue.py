class Queue:

    # Initialize queue
    def __init__(self, size):
        self.q = [None] * size  # list to store queue elements
        self.capacity = size  # maximum capacity of the queue
        self.front = -1  # front points to front element in the queue if present
        self.rear = -1  # rear points to last element in the queue

    # Function to remove front element from the queue
    def enque(self, value):
        # check for queue overflow
        if self.rear + 1 == self.capacity:
            print("OverFlow!! Terminating Program.")
            exit()
        if self.front == -1:
            self.front == 0
        print("Inserting element...", value)

        self.rear = (self.rear + 1)
        self.q[self.rear] = value

    def show(self):
        print("FRONT")
        i = self.front
        while i <= self.rear:
            print(self.q[i])
            i += 1
        print("REAR")

    def isempty(self):
        if self.front == self.rear:
            return True
        return False


if __name__ == '__main__':
    q = Queue(5)
    while 1:
        print("1. Enter 1 to Enque.")
        print("2. Enter 2 to view data. ")
        print("3. Enter 3 to Check if Queue is empty.")
        print("0. To exit.")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter the data you want in Queue: ")
            q.enque(data)
        if choice == 2:
            q.show()
        if choice == 3:
            if q.isempty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")
        if choice == 0:
            exit()

# Custom Queue implementation in Python
class Queue:

    # Initialize queue
    def __init__(self, size):
        self.q = [None] * size  # list to store queue elements
        self.capacity = size  # maximum capacity of the queue
        self.front = 0  # front points to front element in the queue if present
        self.rear = -1  # rear points to last element in the queue

    # Function to remove front element from the queue
    def enque(self, value):
        # check for queue overflow
        if self.rear + 1 == self.capacity:
            print("OverFlow!! Terminating Program.")
            exit()

        print("Inserting element...", value)

        self.rear = (self.rear + 1)
        self.q[self.rear] = value
        self.count = self.count + 1


if __name__ == '__main__':
    q = Queue(5)
    while 1:
        print("1. Enter 1 to Enque.")
        print("0. To exit.")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter the data you want in Queue: ")
            q.enque(data)
        if choice == 0:
            exit()

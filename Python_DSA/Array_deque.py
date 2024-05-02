# Custom Queue implementation in Python
class Queue:

    # Initialize queue
    def __init__(self, size):
        self.q = [None] * size		# list to store queue elements
        self.capacity = size  		# maximum capacity of the queue
        self.front = -1				# front points to front element in the queue if present
        self.rear = -1				# rear points to last element in the queue

# Function to remove front element from the queue
    def enque(self, value):
    # check for queue overflow
        if self.rear + 1 == self.capacity:
            print("OverFlow!! Terminating Program.")
            return
        if self.front == -1:
            self.front == 0

        print("Inserting element...", value)
        self.rear = (self.rear + 1)
        self.q[self.rear] = value

    def show(self):
        if self.isempty():
            print("Queue is empty.")
        else:
            print("FRONT")
            i = self.front
            while i <= self.rear:
                print(self.q[i])
                i += 1
            print("REAR")

    def dequeue(self):
        if self.isempty():
            print("Queue is empty.")
        else:
            print("Deleted element from queue is: ", end=" ")
            x = self.q[self.front]
            self.front = self.front + 1
            return x

    def isempty(self):
        if self.front == self.rear:
            return True
        return False


if __name__ == '__main__':
    q = Queue(5)
    while 1:
        print("1. Enter 1 To Enqueue.")
        print("2. Enter 2 To show the Queue Data. ")
        print("3. Enter 3 To delete the data.")
        print("0. To exit.")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter the data you want in Queue: ")
            q.enque(data)
        if choice == 2:
            q.show()
        if choice == 3:
            val = q.dequeue()
            print(val)
        if choice == 0:
            exit()

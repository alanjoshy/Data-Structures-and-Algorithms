class QueueWithStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        # Add the item to stack1 (end of the queue)
        print(f"{item} enqueued")
        self.stack1.append(item)

    def dequeue(self):
        # Remove item from the front of the queue
        if not self.stack1 and not self.stack2:
            print("Queue is empty")
            return None
        # Transfer elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Pop the front element from stack2
        item = self.stack2.pop()
        print(f"{item} dequeued")
        return item

    def display(self):
        # Display the queue from front to rear
        print("Queue from front to rear:", end=" ")
        if self.stack2:
            for item in reversed(self.stack2):
                print(item, end=" ")
        if self.stack1:
            for item in self.stack1:
                print(item, end=" ")
        print()

# Testing QueueWithStack
queue = QueueWithStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()   # Expected output: "Queue from front to rear: 1 2 3"
queue.dequeue()   # Expected output: "1 dequeued"
queue.display()   # Expected output: "Queue from front to rear: 2 3"

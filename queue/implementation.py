class Queue:
    def __init__(self):
        self.queue = []
    
    # Enqueue operation to add an element at the end of the queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
    
    # Dequeue operation to remove an element from the front of the queue
    def dequeue(self):
        if len(self.queue) < 1:
            return "Queue is empty"
        return self.queue.pop(0)
    
    # Display the elements of the queue
    def display(self):
        print("Queue:", self.queue)
    
    # Get the size of the queue
    def size(self):
        return len(self.queue)


# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()  # Output should show the queue with elements [1, 2, 3]
print("Dequeued:", q.dequeue())  # Output should remove and show 1
q.display()  # Output should show the queue with elements [2, 3]

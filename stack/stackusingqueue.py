class StackWithQueue:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, item):
        # Add the item to queue1 (top of the stack)
        print(f"{item} pushed to stack")
        self.queue1.append(item)

    def pop(self):
        # Remove item from the top of the stack
        if not self.queue1:
            print("Stack is empty")
            return None
        # Transfer all elements but the last one from queue1 to queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        # The last element in queue1 is the top of the stack
        item = self.queue1.pop(0)
        print(f"{item} popped from stack")
        # Swap the queues
        self.queue1, self.queue2 = self.queue2, self.queue1 
        return item

    def display(self):
        # Display the stack from top to bottom
        print("Stack from top to bottom:", end=" ")
        for item in reversed(self.queue1):
            print(item, end=" ")
        print()

# Testing StackWithQueue
stack = StackWithQueue()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()   # Expected output: "Stack from top to bottom: 3 2 1"
stack.pop()       # Expected output: "3 popped from stack"
stack.display()   # Expected output: "Stack from top to bottom: 2 1"

class PriorityQueueUsingList:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        # Append the item along with its priority
        self.queue.append((priority, item))
        # Sort the list by priority in ascending order
        self.queue.sort(key=lambda x: x[0], reverse=True)
        print(f"Enqueued item: {item} with priority: {priority}")

    def dequeue(self):
        if not self.queue:
            print("Priority queue is empty")
            return None
        # Dequeue the element with the highest priority (last item in list)
        priority, item = self.queue.pop(0)
        print(f"Dequeued item: {item} with priority: {priority}")
        return item

    def display(self):
        print("Priority Queue (highest priority first):") 
        for priority, item in self.queue:
            print(f"Item: {item}, Priority: {priority}")

# Testing
pq = PriorityQueueUsingList()
pq.enqueue("Task1", 2)
pq.enqueue("Task2", 5)
pq.enqueue("Task3", 1)
pq.display()
pq.dequeue()
pq.display()

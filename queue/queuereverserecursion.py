from queue import Queue

def reverse_queue_recursive(q):
    # Base case: if the queue is empty, return
    if q.empty():
        return   
    # Step 1: Dequeue the front element
    front = q.get()   
    # Step 2: Recursively call to reverse the rest of the queue
    reverse_queue_recursive(q)   
    # Step 3: Enqueue the front element back (which will now be at the back)
    q.put(front)

# Example usage
q = Queue()
for i in range(1, 6):
    q.put(i)  # Enqueue elements 1 to 5

print("Original queue:")
print(list(q.queue))

# Reverse the queue
reverse_queue_recursive(q)

print("Reversed queue:")
print(list(q.queue))

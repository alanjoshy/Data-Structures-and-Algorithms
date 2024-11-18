class QueueBasedLinkedList:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def add_to_end(self, data):
        # Enqueue element to the end of queue1
        self.queue1.append(data)

    def remove_from_front(self):
        # Dequeue element from the front of queue1
        if self.queue1:
            return self.queue1.pop(0)
        return "List is empty"

    def get_last(self):
        if not self.queue1:
            return "List is empty"
        
        # Transfer elements from queue1 to queue2 until the last element
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        # The last element in queue1 is the last element in the list
        last_element = self.queue1.pop(0)
        self.queue2.append(last_element)
        
        # Restore queue1 from queue2
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        
        return last_element
 
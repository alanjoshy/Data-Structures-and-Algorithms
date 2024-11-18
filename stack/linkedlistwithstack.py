class StackBasedLinkedList:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add_to_end(self, data):
        self.stack1.append(data)

    def remove_from_end(self):
        if self.stack1:
            return self.stack1.pop()
        return "List is empty"

    def get_first(self):
        if not self.stack1:
            return "List is empty"
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        first_element = self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return first_element

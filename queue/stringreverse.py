from queue import Queue

def reverse_string_using_queue(string):
    queue = Queue()
    
    # Step 1: Enqueue all characters of the string
    for char in string:
        queue.put(char)
    
    # Step 2: Use a stack to reverse the characters
    stack = []
    while not queue.empty():
        stack.append(queue.get())
    
    # Step 3: Construct the reversed string by popping from stack
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage
input_string = "Hello"
print("Original String:", input_string)
print("Reversed String:", reverse_string_using_queue(input_string))

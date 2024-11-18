def reverse_string_using_stack(input_string):
    # Initialize an empty stack
    stack = []
    
    # Push each character of the string onto the stack
    for char in input_string:
        stack.append(char)
    
    # Pop characters from the stack and collect them in reverse order
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage
input_string = "hello"
reversed_string = reverse_string_using_stack(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)

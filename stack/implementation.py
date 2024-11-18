stack = []

def push():
    element = input("Enter the element to push: ")
    stack.append(element)
    print("Stack after push:", stack)

def pop():
    if is_empty():
        print("Stack is empty")
    else:
        e = stack.pop()
        print("Popped element:", e)
        print("Stack after pop:", stack)

def peek():
    if is_empty():
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

def is_empty():
    return len(stack) == 0

def display():
    if is_empty():
        print("Stack is empty")
    else:
        print("Current stack:", stack)

while True:
    print("\nSelect operation:\n1. Push\n2. Pop\n3. Peek\n4. Display\n5. Quit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select a valid operation.")

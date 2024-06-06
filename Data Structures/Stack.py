class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None  # or raise an exception
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None  # or raise an exception
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()  # Output: [10, 20, 30]
    print("Popped item:", s.pop())  # Output: Popped item: 30
    s.display()  # Output: [10, 20]
    print("Top item:", s.peek())  # Output: Top item: 20
    print("Stack size:", s.size())  # Output: Stack size: 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" -> " if temp.next else "")
            temp = temp.next
        print()

# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()  # Output: 10 -> 20 -> 30
    print("Dequeued:", q.dequeue())  # Output: Dequeued: 10
    q.display()  # Output: 20 -> 30
    print("Front item is:", q.peek())  # Output: Front item is: 20
    q.dequeue()
    q.dequeue()
    q.display()  # Output: Queue is empty
    print("Dequeued:", q.dequeue())  # Output: Queue is empty; Dequeued: None

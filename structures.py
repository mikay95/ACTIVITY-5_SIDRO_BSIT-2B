class Node:
    """Node structure for singly linked list implementations."""
    def __init__(self, value):
        self.value = value
        self.next = None


class ArrayStack:
    """Fixed-capacity stack using an array (Python list)."""
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: Cannot push to a full stack.")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from an empty stack.")
        value = self.data[self.top]
        self.data[self.top] = None  # Clear reference
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: Cannot peek.")
        return self.data[self.top]

    def display(self):
        if self.is_empty():
            return "Stack: [] (empty)"
        elements = [str(self.data[i]) for i in range(self.top, -1, -1)]
        return f"Stack (Top -> Bottom): [{' -> '.join(elements)}]"


class LinkedStack:
    """Dynamic stack using a singly linked list (operated at the head)."""
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from an empty stack.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: Cannot peek.")
        return self.top.value

    def display(self):
        if self.is_empty():
            return "Stack: [] (empty)"
        curr = self.top
        elements = []
        while curr:
            elements.append(str(curr.value))
            curr = curr.next
        return f"Stack (Top -> Bottom): [{' -> '.join(elements)}]"


class ArrayQueue:
    """Circular queue using an array (Python list) and modulo arithmetic."""
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: Cannot enqueue to a full queue.")
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: Cannot dequeue from an empty queue.")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: Cannot peek.")
        return self.data[self.front]

    def display(self):
        if self.is_empty():
            return f"Queue: {self.data} | Size: 0 (empty)"
        elements = []
        for i in range(self.size):
            idx = (self.front + i) % len(self.data)
            elements.append(str(self.data[idx]))
        return f"Queue (Front -> Rear): [{' -> '.join(elements)}] | Raw Array: {self.data}"


class LinkedQueue:
    """Dynamic queue using a singly linked list with front (head) and rear (tail) pointers."""
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: Cannot dequeue from an empty queue.")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: Cannot peek.")
        return self.front.value

    def display(self):
        if self.is_empty():
            return "Queue: [] (empty)"
        curr = self.front
        elements = []
        while curr:
            elements.append(str(curr.value))
            curr = curr.next
        return f"Queue (Front -> Rear): [{' -> '.join(elements)}]"

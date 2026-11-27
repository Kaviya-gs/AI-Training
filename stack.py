class Stack:
    def _init_(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        print(value, "pushed into stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow: stack is empty")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack (bottom -> top):", self.items)

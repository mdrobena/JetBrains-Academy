class Stack():

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.insert(0, el)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def is_empty(self):
        return self.stack == []

import sys


class Stack:

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        pass

    def peek(self):
        pass


class StackMin(Stack):
    def __init__(self, top=None):
        super(StackMin, self).__init__(top)
        self.min_stack = Stack()

    def minimum(self):
        if self.min_stack.top is None:
            return sys.maxsize
        else:
            return self.min_stack.peek()

    def push(self, data):
        super(StackMin, self).push(data)
        if data < self.minimum():
            self.min_stack.push(data)

    def pop(self):
        pass
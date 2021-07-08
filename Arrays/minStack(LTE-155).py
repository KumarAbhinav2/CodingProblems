"""
Design a stack that supports push, pop, top, and min in O(1).


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x: int) -> None:
        if not self._stack:
            self._stack.append([x, x])
            return
        current_min = self._stack[-1][1]
        self._stack.append([x, min(x, current_min)])

    def pop(self) -> None:
        return self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]


class MinStack2:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, data):
        self.stack.append(data)
        if data < self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self):
        if not self.stack:
            return None
        data = self.stack.pop()
        if data == self.min_stack[-1]:
            self.min_stack.pop()
        return data

    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

    def top(self):
        return self.stack[-1]
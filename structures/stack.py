'''

stack.py
--------

This module contains the Stack class, which is an implementation of the stack data structure.
'''

class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def __str__(self):
        return str(self.stack)


if __name__ == '__main__':

    stack = Stack()
    stack.push(1)
    stack.push(3)
    print(stack)
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
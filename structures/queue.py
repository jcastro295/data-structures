'''

queue.py
--------

This module contains the Queue class, which is an implementation of the queue data structure.
'''


class Queue():
    def __init__(self):
        self.queue = list()

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.queue:
            return self.queue.pop()
        else:
            return None
            
    def get_size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)    


if __name__ == '__main__':

    queue = Queue()
    queue.enqueue(5)
    print(queue)
    queue.enqueue(10)
    print(queue)
    queue.enqueue(15)
    print(queue)
    print(queue.dequeue())
    print(queue)
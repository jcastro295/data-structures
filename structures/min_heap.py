'''

min_heap.py
-----------

This module contains the MinHeap class, which is an implementation of the min heap data structure.
'''

class MinHeap():
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__float_up(len(self.heap)-1)
            
    def push(self, data):
        self.heap.append(data)
        self.__float_up(len(self.heap)-1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return None

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap)-1)
            min_ = self.heap.pop()
            self.__bubble_down(1)
        elif len(self.heap) == 2:
            min_ = self.heap.pop()
        else:
            min_ = False
        return min_

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float_up(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] < self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)

    def __bubble_down(self, index):
        left = index*2
        right = index*2 + 1
        shortest = index
        if len(self.heap) < left and self.heap[shortest] > self.heap[left]:
            shortest = left
        if len(self.heap) < right and self.heap[shortest] > self.heap[right]:
            shortest = right
        if shortest != index:
            self.__swap(index, shortest)
            self.__bubble_down(shortest)

    def __str__(self):
        return str(self.heap[1:])


if __name__ == '__main__':

    heap = MinHeap([95, 3, 21])
    heap.push(10)
    print(heap)
    print(heap.pop())
    print(heap.peek())
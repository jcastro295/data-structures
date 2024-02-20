'''

max_heap.py
-----------

This module contains the MaxHeap class, which is an implementation of the max heap data structure.
'''

class MaxHeap():
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
            max_ = self.heap.pop()
            self.__bubble_down(1)
        elif len(self.heap) == 2:
            max_ = self.heap.pop()
        else:
            max_ = False
        return max_

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __float_up(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__float_up(parent)

    def __bubble_down(self, index):
        left = index*2
        right = index*2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubble_down(largest)

    def __str__(self):
        return str(self.heap[1:])


if __name__ == '__main__':

    heap = MaxHeap([95, 3, 21])
    heap.push(10)
    print(heap)
    print(heap.pop())
    print(heap.peek())
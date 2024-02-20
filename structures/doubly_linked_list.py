'''

doubly_linked_list.py
---------------------

This module contains the DoublyLinkedList class, which is an implementation of the doubly linked list data structure.
'''


class Node():
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
    
    def __str__(self):
        return str('(' + str(self.data) + ')')


class DoublyLinkedList():
    
    def __init__(self, root=None):
        self.root = root
        self.last = root
        self.size = 0
    
    def add(self, data):
        if self.size == 0:
            self.root = Node(data)
            self.last = self.root
        else:
            new_node = Node(data, self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size += 1
        
    def find(self, data):
        this_node = self.root
        while this_node:
            if this_node.data == data:
                return data
            elif not this_node.next_node:
                return False
            else:
                this_node = this_node.next_node
    
    def remove(self, data):
        this_node = self.root
        while this_node:
            if this_node.data == data:
                if this_node.prev_node:
                    if this_node.next_node: # delete a middle node
                        this_node.prev_node.next_node = this_node.next_node
                        this_node.next_node.prev_node = this_node.prev_node
                    else: # delete last node
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node
                else: # delete root node
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -= 1
                return True # data remove
            else:
                this_node = this_node.next_node
        return False
                
    
    def print_list(self):
        if not self.root:
            return
        this_node = self.root
        print(this_node, end='=>')
        while this_node.next_node:
            this_node = this_node.next_node
            print(this_node, end='=>')
        print()


if __name__ == '__main__':

    doubly_linked_list = DoublyLinkedList()
    for i in [5, 9, 3, 8, 9]:
        doubly_linked_list.add(i)

    print('size='+str(doubly_linked_list.size))
    doubly_linked_list.print_list()
    doubly_linked_list.remove(8)
    print('size='+str(doubly_linked_list.size))


    print()
    print(doubly_linked_list.remove(15))
    print(doubly_linked_list.find(15))
    doubly_linked_list.add(21)
    doubly_linked_list.add(22)
    doubly_linked_list.remove(5)
    doubly_linked_list.print_list()
    print(doubly_linked_list.last.prev_node)
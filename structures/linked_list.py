'''

linked_list.py
--------------

This module contains the LinkedList class, which is an implementation of the linked list data structure.
'''

class Node():
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
    
    def __str__(self):
        return str('(' + str(self.data) + ')')


class LinkedList():
    
    def __init__(self, root=None):
        self.root = root
        self.size = 0
    
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
        
    def find(self, data):
        this_node = self.root
        while this_node:
            if this_node.data == data:
                return data
            else:
                this_node = this_node.next_node
        return None
    
    def remove(self, data):
        this_node = self.root
        prev_node = None
        
        while this_node:
            if this_node.data == data:
                if prev_node:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False
    
    def print_list(self):
        this_node = self.root
        while this_node:
            print(this_node, end='=>')
            this_node = this_node.next_node
        print('None')


if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.add(5)
    linked_list.add(8)
    linked_list.add(12)
    linked_list.print_list()

    print('size='+str(linked_list.size))
    linked_list.remove(8)
    print('size='+str(linked_list.size))
    print(linked_list.find(5))
    print(linked_list.root)
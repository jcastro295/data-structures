'''

binary_tree.py
--------------

This module contains the BinaryTree class, which is an implementation of the binary tree data structure.
'''

class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def insert(self, data):
        if self.data == data:
            return False # duplicate value
        elif self.data > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = BinaryTree(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = BinaryTree(data)
                return True

    def find(self, data):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        elif self.data < data:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def get_size(self):
        if self.left and self.right:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1

    def preorder(self):
        if self:
            print(self.data, end=' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.data, end=' ')
            if self.right:
                self.right.inorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.data, end=' ')


if __name__ == '__main__':

    tree = BinaryTree(7)
    tree.insert(9)

    for i in [15, 10, 2, 12, 3, 1, 13, 6, 11, 4, 14, 9]:
        tree.insert(i)
    for i in range(16):
        print(tree.find(i), end=' ')
    print('\n', tree.get_size())

    tree.preorder()
    print()
    tree.inorder()
    print()
    tree.postorder()
    print()
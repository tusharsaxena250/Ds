# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:43:05 2020

@author: Tushar Saxena
"""

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val =  val
        
class Tree:
    def __init__(self):
        self.root = None
        
    def getRoot(self):
        return self.root
    
    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)
            
    def _add(self, val, node):
        if val < node.val:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)
    
    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        
    def _find(self, val, node):
        if val == node.val:
            print("Found")
        elif val < node.val and node.left is not None:
            self._find(val, node.left)
        elif val > node.val and node.right is not None:
            self._find(val, node.right)
        else:
            print("Not Found")
            
    def deleteTree(self):
        self.root = None
        print("Tree Deleted!")
    
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
            
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print('|          ', str(node.val), '          |')
            self._printTree(node.right)
            
            
tree = Tree()
           
while True:
    print('1: Print Tree')
    print('2: Add Element')
    print('3: Delete Tree')
    print('4: Find Element')
    print('0: Exit')
    
    choice = int(input("Enter your choice."))
    
    if choice == 1:
        tree.printTree()
    elif choice == 2:
        val = int(input("Enter the value to be added!"))
        tree.add(val)
    elif choice == 3:
        tree.deleteTree()
    elif choice == 4:
        val = int(input("Enter the value to be found!"))
        tree.find(val)
    elif choice == 0:
        break
    else:
        print("Enter valid choice!")
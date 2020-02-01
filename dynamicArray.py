# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:49:53 2020

@author: Tushar Saxena
"""

class Array:
    def __init__(self, cap):
        self.capacity = cap
        self.arr = []
        self.length = len(self.arr)
    
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def insert(self, value):
        if len(self.arr) < self.capacity: 
            self.arr.append(value)
            self.length = len(self.arr)
        else:
            print("Capacity reached")
            self.capacity = 2 * self.capacity
            self.arr.append(value)
    
    def removeAt(self, index):###########Error##############
        if index > self.capacity:
            print("Index out of bound!")
        else:
            temp = Array(self.capacity - 1)
            for i in self.arr[:index] and self.arr[index + 1:]:
                temp.append(i)
            self.arr =  temp
            self.length = temp.size()
            self.capacity = self.capacity - 1
            
    def size(self):
        return self.length
    
    def getElem(self, index):
        return self.arr[index]
    
    def setElem(self, index, value):
        self.arr[index] = value
    
    def indexOf(self):
        pass
    
    def contains(self, value):
        if value in self.arr:
            return True
        else:
            return False
        
    def toString(self):
        return ' '.join(str(i) for i in self.arr)
    
    def clear(self):
        self.arr = []
        self.length = 0
    
    def printArray(self):
        return (self.arr)

# a = Array(1)
# a.insert(12)
# a.insert(9)
# a.printArray()

# a.toString()

# a.contains(9)

# a.setElem(1, 24)
# a.getElem(1)
# a.printArray()
# a.isEmpty()
# a.clear()
# a.printArray()
# a.isEmpty()

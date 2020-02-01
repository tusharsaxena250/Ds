# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:10:54 2020

@author: Tushar Saxena
"""

#using classes
class Stack:
    def __init__(self):
        self.items = []
    def is_enpty(self):
        return (self.items == [])
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    
s = Stack()    

while True:
    print('1: Print Array')
    print('2: Add Element')
    print('3: Delete Element')
    print('4: Exit')
    
    choice = int(input("Enter your choice."))
    
    if choice == 1:
        print(s.items)
    elif choice == 2:
        val = int(input("Enter the value to be added!"))
        s.push(val)
    elif choice == 3:
        if s.is_empty():
            print(s.pop())
    elif choice == 4:
        break
    else:
        print("Enter valid choice!")
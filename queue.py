# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 13:24:23 2020

@author: Tushar Saxena
"""

class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return (self.items == [])
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.remove(self.items[0])
  
q = Queue()

while True:
    print('1: Print Array')
    print('2: Add Element')
    print('3: Delete Element')
    print('4: Exit')
    
    choice = int(input("Enter your choice."))
    
    if choice == 1:
        print(q.items)
    elif choice == 2:
        val = int(input("Enter the value to be added!"))
        q.push(val)
    elif choice == 3:
        if q.is_empty():
            print("Empty queue")
        else:
            print(q.pop())
    elif choice == 4:
        break
    else:
        print("Enter valid choice!")

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:59:36 2020

@author: Tushar Saxena
"""

import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
while True:
    print('1: Print Array')
    print('2: Add Element')
    print('3: Delete Element')
    print('4: Exit')
    
    choice = int(input("Enter your choice."))
    
    if choice == 1:
        for n in a:
            print(n)
    elif choice == 2:
        val = int(input("Enter the value to be added!"))
        if isinstance(val, int):
            a.append(val)
    elif choice == 3:
        val = a.pop()
        print("Value popped: ", val)
    elif choice == 4:
        break
    else:
        print("Enter valid choice!")
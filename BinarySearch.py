# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:01:24 2020

@author: Tushar Saxena
"""

"""
Algo:
    low:= 0 
    high:= n-1
    while low <= high Do
        mid = (low + high) / 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
    return -1 #value not found
    
O(log(n))
"""


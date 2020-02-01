# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:59:36 2020

@author: Tushar Saxena
"""
#Find sum of numbers from different arrays closest to given sum
import time 
a = [-1, 3,8, 2, 9, 5]
b = [4, 1, 2, 10, 5, 20]

c = 24 #given sum

summ = 0
diff = c
start = time.time()

x = 0
y = 0

for i in a:
    for j in b:
        summ = i + j
        if abs(c - summ) < diff:
            x = i
            y = j
            diff = abs(c - summ)
        
print(x, y, summ, diff)
end = time.time()
print(end - start)


##alternate
summ = 0
diff = c
start = time.time()

x = 0
y = 0

while a:
    i = max(a)
    j = max(b)
    
    summ = i + j
    if abs(c - summ) < diff:
        diff = abs(c - summ)
        x = i
        y = j
    else:
        a.remove(i)
        b.remove(j)
        
print(x, y, summ, diff)
end = time.time()
print(end - start)
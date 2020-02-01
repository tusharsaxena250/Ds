#return all(i < j for i in range(n))

#hash table

arr = ["a", "a", "c", "b"]

fltr = dict()

for i in arr:
    fltr[i] = 0
    
result = set(fltr.keys())
print(result)

#counting

arr = [1, 2, 3, 4, 5, 5, 3, 1]


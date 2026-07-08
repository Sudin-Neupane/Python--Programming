import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# select a single element
simple_indexing = a[3]
print("Simple Indexing:",simple_indexing) # 4
# select multiple elements
fancy_indexing = a[[1, 2, 5, 7]]
print("Fancy Indexing:",fancy_indexing) # [2 3 6 8]
#Returns array of indices of sorted array in ascending order
print("Indicies of Sorted Data:",np.argsort(a))
# sort a using fancy indexing
sorted_array = a[np.argsort(a)]
print("Sorted Data:",sorted_array)
#Sorting is descending order
sorted_array = a[np.argsort(-a)]
print("Reverse Sorted Data",sorted_array)

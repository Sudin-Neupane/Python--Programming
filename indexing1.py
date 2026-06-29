import numpy as np
a = np.arange(10)
print("Array Elements:")
print(a)
print("Element at index 3")
print(a[3])
print("Element from index 3-6")
print(a[3:7])
a[2]=10 #modifying element at index 2
a[4:6]=11 #modifying element from index 4 to 5
print("Array Elements:")
print(a)
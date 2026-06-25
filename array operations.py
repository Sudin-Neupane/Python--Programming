import numpy as np

a = np.array([1., 2., 3., 4., 5., 6.])
print(a)

r = a * a
print("Element-wise multiplication of arrays:")
print(r)

r = a + a
print("Sum of arrays:")
print(r)

r = a / 2
print("Half of array elements:")
print(r)

r = a**0.5
print("Square root of array elements:")
print(r)

print("Array Elements:")
print(a)
print("Element at index 3")
print(a[3])
print("Element from index 3 to 5")
print(a[3:6])

a[2] = 10  # modifying element at index 2
a[4:6] = 11  # modifying elements from index 4 to 5
print("Array Elements:")
print(a)

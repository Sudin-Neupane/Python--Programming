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

print("Array Elements: xyz")
print(a)
print("Element at index 3")
print(a[3])
print("Element from index 3 to 6")
print(a[3:6])

a[2] = 10  # modifying element at index 2
a[4:6] = 11 ,12  # modifying elements from index 4 to 5
print("Array Elements:")
print(a)
print("this is the following learning steps ")
a = np.array([1,2,3,4,5,6,7,8,9])
aslice=a[1:7]
aslice[4]=18 #modification will be reflected in original array
print("Array Elements:")
print(a)
a =np.array([1,2,3,4,5,6,7,8,9])
aslice=a[3:7]
aslice[1]=15 #modification will  be reflected in original array
print("Array Elements:")
print(a)
a = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print ("Array Elements: of 3 array")
print(a)
print("Array Element at index 2")
print(a[1][1])
print("Array Element at index 1,2")
print(a[1][2])
print(a[1,2])#Equivalent to a[1][2]

a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Array Elements for the new matrix ")
print(a)
print("Array Element at index 1")
print(a[0])
print("Array Element at index 1,1")
print(a[0,1])
print("Array Element at index 1,1,2")
print(a[1,1,2])

#create array of length 5
import numpy as np
data=np.zeros(5)
print(data)
#create array of length 5
data=np.ones(5)
print(data)
#create array of shape(3,3)
data=np.zeros((3,3))
print(data)
#create array of shape(3,3)
data=np.ones((3,3))
print(data)
#create array of length 10
data=np.empty(10)
print(data)
#create array of shape(2,3)
data=np.empty((2,3))
print(data)
data=np.arange(10)
print(data)
data=np.full((3,3), 8)
print(data)
data = np.identity(3)
print(data)
#create array with elements 0-9
data=np.arange(10)
print(data)
#create array with elements 5-9
data=np.arange(5,10)
print(data)
#create array with elements 1-9
data=np.arange(4,10,2)
print(data)
#create array with elements 0-9
data=np.arange(10)
print(data)
d=np.ones_like(data)
print(d)


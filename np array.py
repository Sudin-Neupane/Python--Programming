#create array of length 5
import numpy as np
da=np.zeros(5)
print(da)
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
#creates identity matrix of 3x3
data=np.eye(3)
print(data)
#creates identity matrix of 4x
data=np.identity(4)
print(data)
print(da)
data=np.array([1,3,5,8],dtype='int64')
print(data)
data=np.array([1,3,5,8],dtype='int64')
print(data)
data=data.astype('float64')
print(data)
data=data.astype(np.float32)
print(data)

def new_func():
    data=np.array(['2.5','3.7','9.1'],dtype=np.string_)
    print(data)
    data=data.astype('float64')
    print(data)
    print(data.dtype)
data=np.array(['2.5','3.7','9.1f'],dtype=np.string_)
print(data)
data=data.astype('float64') #Error
print(data)
print(data.dtype)

a = np.arange(10)
print("Dataset:",a)
s=np.sqrt(a)#unary universal function
print("Square Roots:",s)
e=np.exp(a)
print("Exp(a):",e)
x=np.random.randn(10)
y=np.random.randn(10)
z=np.maximum(x,y)#bunary universal function
print("x=",x)
print("y=",y)
print("z=",z)
m=np.max(x)
print("Maximum=",m)
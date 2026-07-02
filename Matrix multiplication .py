#Matrix multiplication
import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 23], [-1, 7], [8, 9]])
z=x.dot(y)
print(z)
r=np.dot(x, y)#equivalent to x.dot(y)
print(r)
#solving system of linear equations, finding determinant and inverse
#2x+3y-z=5
#x+3y-z=4
#3x-y+2z=7
import numpy as np
from numpy.linalg import inv, solve,det
a = np.array([[2,3,-1],[1,3,-1],[3,-1,2]])
b=np.array([5,4,7])
s=solve(a,b)
print(s)
d=det(a)
print("determinant of a=",d)
b=inv(a)
print("Inverse of a=",b)

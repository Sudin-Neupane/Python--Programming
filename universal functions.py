import numpy as np
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

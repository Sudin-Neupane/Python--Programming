import pandas as pd
import numpy as np
obj = pd.Series([4, 7, -5, 3]) #series data structure
print(obj.values) #displaying values in the data structure
print(obj[1]) #vaue at index 1
obj[2]=5 #modifying value
print(obj.values)
print(obj[[1,2,3]]) #displaying values at index 1, 2, and 3
obj = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
print(obj.values)
print(obj['a'])
obj=obj*2 # scalar multiplication
print(obj.values)
print(obj[obj>0])#boolean indexing
print(np.exp(obj)) #using universal functions
print(pd.isnull(obj))#checking for null valuess
print(pd.notnull(obj))
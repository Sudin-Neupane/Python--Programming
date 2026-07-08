import numpy as np
a = np.array([12, 24, 16, 21, 32, 29, 7, 15])
print(a)
boolean_mask = a > 20
print(boolean_mask)
print(a[boolean_mask])
a[boolean_mask]=0#sets all elements greater than 20 to zero
print(a)

import numpy as np
np.random.seed(100)
d=np.random.randint(0,10)
print("d=",d)
samples = np.random.normal(size=(4, 4))
print(samples)
d=np.random.permutation([1,2,3])
print("d=",d)
l=[1,2,3,4,5]
d=np.random.shuffle(l)
print("Shuffled List=",l)

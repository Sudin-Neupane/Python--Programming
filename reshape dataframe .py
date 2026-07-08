import pandas as pd
df1 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=list('bcd'),

index=['1', '2', '3'])

df2 = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=list('bde'),

index=['1', '2', '3', '4'])

print(df1)
print(df2)
df=df1+df1
print(df)

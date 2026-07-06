import pandas as pd
data = {'State': ['hydrogen ', 'Helium ', 'Lithium', 'Beryllium', 'Boron'],

'Year': [1, 2, 3, 4, 5]}
frame1 = pd.DataFrame(data)#creating dataframe
print(frame1)
frame2 = pd.DataFrame(data,columns=["State","Year","Debt"])
print(frame2)#creating data frame
print(frame2["State"])#displaying column State
obj=pd.Series([2,5,3,3,4])
frame2["Debt"]=obj
print(frame2)#displaying data frame
print(frame2.values)#displaying in 2D array format5
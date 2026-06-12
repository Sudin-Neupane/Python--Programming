#Zip
list1=['a','b','c']
list2=[1,2,3]
list3=list(zip(list1,list2))
print("Zipped List:",list3)
l1,l2=zip(*list3)
print("First List:",l1)
print("Second List:",l2)

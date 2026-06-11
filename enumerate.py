# enumerate function
l1 = ["eat", "sleep","code" ,"repeat"]
s1 = "sdn"
# creating enumerate objects
obj1 = enumerate(l1,1)
obj2 = enumerate(s1,1)
print (obj1)
print (obj2)

for position,task in list(obj1):
 print(position,task)
for position,task in list(obj2):
    print(position,task)
print(obj2)

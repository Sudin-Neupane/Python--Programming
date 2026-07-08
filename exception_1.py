l=[3,4,2,1,5]
try:
    print("List Elements:")
    for i in range(5):
        print(l[i])
    print("Squared List Elements:")
    for i in range(6):
        print(l[i]*l[i])
except IndexError:
    print("Invalid Index!!!!")
    
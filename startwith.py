import re
txt = input("Enter String:")
x = re.search("^B *", txt)
if x:
 print("String starts with B")
else:
 print("String does not start with B")

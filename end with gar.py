import re
txt = input ("Enter String:")
x = re.search("^B.*gar$", txt)
if x:
 print("String starts with B and ends with gar")
else:
 print("String does not start with B or does not end with gar")
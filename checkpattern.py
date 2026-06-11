from ast import pattern
import re
email = input("Enter email: ")
pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
if re.fullmatch(pattern, email):
    print("Valid Gmail address")
else:
    print("Not a Gmail address")

    
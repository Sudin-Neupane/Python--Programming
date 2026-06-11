#Validity of cell number
from os import path
import re
cell=input("Input Cell Number:")
pat = '\d{10}'
if(re.fullmatch(pat,cell)):
 print("Valid Cell Number")
else:
 print("Invalid Cell Number")
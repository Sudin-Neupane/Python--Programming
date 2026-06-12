import csv
from pathlib import Path

file_path = Path(r"C:\Users\SANJIV NEUPANE\Downloads\filee.csv")

with file_path.open('r', newline='', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    for rec in csv_reader:
        print(rec)

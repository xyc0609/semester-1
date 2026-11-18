# Worksheet 1.2: Task 1 Solution
import sys
try:
    grade = int(input("Please enter your grade: "))
except ValueError:
    sys.exit("Error: Grade must be an integer between 0 and 100.")
    
if not 0 <= grade <= 100:
    sys.exit("Error: Grade must be an integer between 0 and 100.")
    
if 70<= grade <= 100:
    print(f"{grade} is a Distinction.")
elif 40 <= grade <= 69:
    print(f"{grade} is a Pass.")
else:
    print(f"{grade} is a Fail.")

    
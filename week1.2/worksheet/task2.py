# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)

numbers.sort()

if len(numbers) % 2 == 0:
    middle1 = numbers[len(numbers) // 2 - 1]
    middle2 = numbers[len(numbers) // 2]
    median = (middle1 + middle2) / 2
else:
    median = numbers[len(numbers) // 2]

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Mean =", mean)
print("Median =", median)
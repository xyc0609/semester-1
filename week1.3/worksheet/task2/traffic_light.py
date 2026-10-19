"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Yuchao Xu
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps
cycle_time = sum(states.values())
# At the end of each step you should output the time and state using the statement on line 14
for systime in range (1, maxtime + 1):
    elapsed = (systime -1) % cycle_time

    if elapsed <= 2 or elapsed == 14:
        state = "red"
    elif elapsed < 6:
        state = "red_amber"
    elif elapsed < 11:
        state = "green"
    else:
        state = "amber"
    print(f"Time {systime:03} State {state}")


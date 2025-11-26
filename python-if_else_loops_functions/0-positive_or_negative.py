#!/usr/bin/python3

# Test cases
for number in [98, -98, 0]:
    if number > 0:
        print(f"{number} is positive")
    elif number == 0:
        print(f"{number} is zero")
    else:
        print(f"{number} is negative")

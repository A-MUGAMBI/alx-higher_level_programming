#!/usr/bin/python3
""""a program that write the numbers form 0 - 99 in ascending order."""
for number in range (0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")

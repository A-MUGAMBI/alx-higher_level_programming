#!/usr/bin/python3


"""a program that checks for upper case and lower case charactrs"""

"""Author Tonny"""

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

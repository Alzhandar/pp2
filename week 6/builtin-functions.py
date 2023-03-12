from functools import reduce
import time
import math
# Write a Python program with builtin function to multiply all the numbers in a list
def multiply_list(numbers):
    return reduce(lambda x, y: x*y, numbers)
l=list(map(int,input().split()))
rez=multiply_list(l)
print(rez)
# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_up_low(string):
    up_count=0
    low_count=0
    for char in string:
        if char.isupper():
            up_count+=1
        elif char.islower():
            low_count+=1
    return (up_count,low_count)
s="Hello my name is Alzhan"
rez=count_up_low(s)
print(rez)
# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def is_palindrome(string):
    reversed_string=''.join(reversed(string))
    if string==reversed_string:
        return True
    else:
        return False
s="radar"
rez=is_palindrome(s)
if rez:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
# Write a Python program that invoke square root function after specific milliseconds.
def square_milliseconds(n, milliseconds):
    time.sleep(milliseconds / 1000)
    rez=math.sqrt(n)
    return rez
n=36600
milliseconds=2123
rez=square_milliseconds(n, milliseconds)
print(f"Square root of {n} after {milliseconds} milliseconds is {rez}")

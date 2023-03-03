import math


n=int(input("Input number of sides:"))
l=int(input("Input the length of a side:"))
S=(n*l**2)/(4*math.tan(math.pi/n))
print(int(S))
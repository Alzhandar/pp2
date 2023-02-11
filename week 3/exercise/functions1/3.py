def solve(numheads,numlegs):
    y=(numlegs-2*numheads)/2
    x=numheads-y
    return int(y),int(x)
a=int(input())
b=int(input())
print(solve(a,b))
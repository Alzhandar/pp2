x=[0,1]
i=2
l=int(input())
while i <= l:
    x.append(x[i-1]+x[i-2])
    i+=1
if(l==0):
    print("0")
else:
    print(x[-1])
sum=0
rez=1
n=int(input())
for i in range (1,n+1) :
    rez*=i
    sum+=rez
print(sum)
def _iter(n):
    for i in range(1,n+1):
        if i%3==0 and i%4==0:
            print(i)
a=int(input())
_iter(a)
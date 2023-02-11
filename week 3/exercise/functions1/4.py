from random import randrange

def createList(n,_from,_to):
    l=[0]*n
    for i in range(n):
        l[i]=randrange(_from,_to+1)
    return l
def filter_prime(_list):
    l=[]
    for i in _list:
        if i%2==0:
            return True
        else:
            return False
        return i
n=int(input())
f=int(input())
t=int(input())
l=createList(n,f,t)
print(l)
print(filter_prime(l))
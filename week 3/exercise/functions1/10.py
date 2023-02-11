from random import randrange

def createList(n,_from,_to):
    l=[0]*n
    for i in range(n):
        l[i]=randrange(_from,_to+1)
    return l
def unique(_list):
    l=[]
    for i in _list:
        if i in l:
            continue
        else:
            l.append(i)
    return l
n=int(input())
f=int(input())
t=int(input())
l=createList(n,f,t)
print(l)
print(unique(l))
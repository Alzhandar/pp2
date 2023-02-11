from random import randrange

def createList(n,_from,_to):
    l=[0]*n
    for i in range(n):
        l[i]=randrange(_from,_to+1)
    return l
def find(_list):
    l=[]
    for i in range(len(_list)-1):
        for j in range(1,len(l)):
            if(_list[i]==_list[j]):
                return 1
            else:
                return 0
n=int(input())
f=int(input())
t=int(input())
l=createList(n,f,t)
print(l)
print(find(l))
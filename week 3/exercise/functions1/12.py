l=list(map(int,input().split()))
def histogram(_list):
    for i in l:
        for j in range(1,i+1):
            j='*'
            print(j,end=' ') 
        print()
histogram(l)
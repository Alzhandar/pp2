def myfunc(n):
    return abs(n-50)
l=[100,50,65,82,23]
l.sort(key=myfunc)
print(l)
from datetime import datetime, timedelta
n=int(input())
x= datetime.now()
print("Today:",x)
y= x - timedelta(days=n)
print("Then",y)
z = (x - y).total_seconds()
print("seconds:",z)
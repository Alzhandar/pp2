import datetime
x = datetime.datetime.now()
print("Today:",x)
y=x.replace(microsecond=0)
print("Today",y)
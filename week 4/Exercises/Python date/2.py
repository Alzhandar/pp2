import datetime
x = datetime.datetime.now()
print("Today:",x)
y=datetime.timedelta(days=1)
print("Tomorrow:",x+y)
print("Yesterday:",x-y)

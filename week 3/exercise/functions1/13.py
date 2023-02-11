from random import randrange

c=0
print("Hello! What is your name?")
a=input()
print(a)
print("Well, KBTU, I am thinking of a number between 1 and 20.")
a=randrange(1,20)
print("Take a guess.")
x=randrange(1,20)
print(x)
if(x!=a):
    c+=1
print("Your guess is too low.")
print("Take a guess.")
y=randrange(1,20)
print(y)
if(y!=a):
    c+=1

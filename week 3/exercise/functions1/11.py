def palindrom(s):
    string=s[::-1]
    string2=s
    if string==string2:
        return("YES")
    else:
        return("NO")
s=input()
print(palindrom(s))   

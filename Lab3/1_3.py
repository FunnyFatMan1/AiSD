def nwdIIi(a,b):
    while b!=0:
        temp=b
        b=a%b
        a=temp
    return a
print(nwdIIi(12,18))
print(nwdIIi(28,24))
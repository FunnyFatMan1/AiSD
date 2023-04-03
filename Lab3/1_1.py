def nwdIi(a,b):
    while a!=b:
        if a>b: a=a-b
        else: b=b-a

    return a

print(nwdIi(12,18))
print(nwdIi(28,24))
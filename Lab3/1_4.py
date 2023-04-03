def nwdIIr(a,b):
    if b!=0:
        return nwdIIr(b,a%b)
    return a
print(nwdIIr(12,18))
print(nwdIIr(28,24))
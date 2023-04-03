def nwdIr(a,b):
    if a!=b:
        if a>b: return nwdIr(a-b,b)
        else: return nwdIr(a,b-a)

    return a
print(nwdIr(12,18))
print(nwdIr(28,24))
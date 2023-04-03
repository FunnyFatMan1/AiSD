tab = [1,2,3,4,5]

def rev(tab):
    if len(tab)==0:
        return []
    else:
        return [tab[-1]] + rev(tab[:-1])

print(rev(tab))
n=int(input("Podaj wartość n: "))
i=0
tab2=[]
if n>=1:
    while i<n:
        temp=float(input("Wprowadź wartość do tablicy: "))
        if temp >=0 and temp <=200:
            i+=1
            tab2.append(temp)
        else:
            continue

print(tab2)
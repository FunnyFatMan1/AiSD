def binary(n):
    if n==0: return 0
    else:
        liczba = binary(n//2)
        reszta = n%2
        return liczba*10 + reszta

print(binary(16))
'''def fibonacci(n):

    # Warunki elementarne
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Inicjalizacja tablicy wyników
        fib = [0] * (n + 1)
        fib[0] = 0
        fib[1] = 1
        # Obliczanie kolejnych elementów ciągu
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]
print((fibonacci(10)))
print((fibonacci(1)))
print((fibonacci(0)))
print((fibonacci(25)))
print((fibonacci(15)))
print((fibonacci(13)))
wersja chatu
'''

fibl=[]
n=int(input("podaj n dla c.fibonaciego: "))
for i in range(n):
    if i==0:
        fibl.append(i)
    elif i==1:
        fibl.append(i)
    else:
        fibl.append(fibl[i-1]+fibl[i-2])
print(fibl)

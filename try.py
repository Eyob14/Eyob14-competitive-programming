def myPow(x, n):
    total = 1
    if n == 0:
        return 1
    elif n%2 == 0 and (n >= 4):
        return (x**2) * myPow(x, n/2)
    elif n%2 != 0:
        return x * myPow(x**2, (n-1)/2)
print(myPow(2, 2))
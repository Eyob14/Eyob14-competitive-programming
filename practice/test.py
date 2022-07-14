import math
def isPowerOfThree(n):
    if n == 0:
        return False
    elif n < 0:
        if (-1*n) == pow(3, int(math.log((-1*n),3))):
            return True
    elif n > 0 and  (n == pow(3, int(math.log(n,3)))):
        return True
    else:
        return False
print(isPowerOfThree(21))
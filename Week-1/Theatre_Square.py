import math
n, m, a = input().split()
n, m, a = eval(n), eval(m), eval(a)
width = math.ceil(n / a)
height = math.ceil(m / a)
total = math.ceil(width * height)
print(total)
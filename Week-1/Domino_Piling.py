m, n = input().split()
result = 0
def domino(a, b):
    area = int(a) * int(b)
    if area % 2 == 0:
        result = area // 2
    elif area % 2 == 1:
        result = (area - 1) // 2
    return result
 
print(domino(m, n))
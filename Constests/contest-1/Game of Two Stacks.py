def twoStacks(maxSum, a, b):
    answer = 0
    total = 0
    i = j = 0
    while i < len(a) and total + a[i] <= maxSum:
        total += a[i]
        i += 1
        answer += 1
    while j < len(b) and i >= 0:
        total += b[j]
        j += 1
        while i > 0 and total > maxSum:
            i -= 1
            total -= a[i]
        if total <= maxSum and answer < (i + j):
            answer = i + j
    return answer
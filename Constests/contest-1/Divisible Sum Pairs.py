def divisibleSumPairs(n, k, ar):
    # Write your code here
    counter = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                counter += 1
    return counter
cost = [1, 2, 3, 100]
for i in range(len(cost)-1):
    next, value = (i, cost[i]) if cost[i] < cost[i+1] else (i+1, cost[i+1])
    print(next, value)
lst = [1,2,3,4,5,6]
k = 2
t = 0
for i in range(len(lst)):    
    if (i+1) % k == 0:
        temp = lst[t:t+k]
        temp = temp[::-1]
        lst[t:t+k] = temp
        t += k
print(lst)

def brokenChecker(string):
    count = {}
    temp = []
    res = ""
    for i in string:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    for i, j in count.items():
        if (j%2!=0):
            temp.append(i)
        else:
            continue
    temp.sort()
    res = res.join(temp)
    print("{}".format(res))
        
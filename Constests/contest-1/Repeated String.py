def repeatedString(s, n):
    counter = 0
    new = ""
    for i in s:
        if i == 'a':
            counter += 1
    counter *= n//len(s)
    for i in range(n%len(s)):
        new += s[i]
    char = 'a'
    for i in new:
        if i == char:
            counter+=1
    return counter
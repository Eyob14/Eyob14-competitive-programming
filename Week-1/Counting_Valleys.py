def countingValleys(steps, path):
    counter = 0
    level = 0
    for i in path:
        if (i == "D"):
            level += 1
        if (i == "U"):
            level -= 1
        if (level == 0) and (i == "U"):
            counter += 1
    return counter

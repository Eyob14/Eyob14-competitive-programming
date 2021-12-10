def gradingStudents(grades):
    new = []
    for i in grades:
        if i < 38:
            new.append(i)
        else:
            temp = i + (5 - i%5)
            if temp - i < 3:
                i = temp
                new.append(i)
            else:
                new.append(i)
    return new
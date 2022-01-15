def carFleet(target, position, speed):
    p = []
    s = []
    j= 0
    p.append(position[j])
    s.append(speed[j])
    
    for i in range(1, len(position)):
        if (position[i] < p[j] and speed[i] > s[j]):
            t1 = target - p[j]
            t2 = target - position[i]
            if t1 % s[j] == 0 and t2 % speed[i] == 0:
                p[j] = max(position[i], p[j])
                s[j] = min(speed[i], s[j])
            else:
                p.append(position[i])
                s.append(speed[i])
                j += 1
    return j
        
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(carFleet(target, position, speed))
def kClosest(points, k):
    last = []
    result = []
    def distance(x):
        return (x[0]**2 + x[1]**2)**0.5
   
    points.sort(key=distance)
    return points[:k]
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points, k))

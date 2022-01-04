class Solution:
    def distance(self, x):
        result = x[0]*x[0] + x[1]*x[1] 
        return result
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=self.distance)
        return points[:k]
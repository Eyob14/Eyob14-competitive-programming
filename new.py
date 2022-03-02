import heapq
class MedianFinder:

    def __init__(self):
        self.heap_min = []
        self.heap_max = []

    def addNum(self, num: int) -> None:
        if len(self.heap_max) == len(self.heap_min):
            heapq.heappush(self.heap_max, -heapq.heappushpop(self.heap_min, num))
        else:
            heapq.heappush(self.heap_min, -heapq.heappushpop(self.heap_max, -num))
        print("min:", self.heap_min)
        print("max:", self.heap_max)
        print()

    def findMedian(self) -> float:
        if len(self.heap_max) > len(self.heap_min):
            return -self.heap_max[0]
        else:
            return (-self.heap_max[0] + self.heap_min[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
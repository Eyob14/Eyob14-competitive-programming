import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
    def add(self, val: int) -> int:
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        if self.k > len(self.nums):
            heapq.heappush(self.nums, val)
        else:
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
        return self.nums[0]

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = sum(matrix, [])
        nums = [-1 * i for i in nums]
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return -1 * nums[0]

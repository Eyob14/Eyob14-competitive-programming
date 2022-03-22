import math
from typing import List
class Solution:
    def summation(self, arr, mid):
        total = 0
        for i in arr:
            division = math.ceil(i/mid)
            total += division
        return total
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums) + 1
        while (left <= right):
            mid = left + (right - left)//2
            value = self.summation(nums, mid)
            if value <= threshold:
                right = mid - 1
            else:
                left = mid + 1
        return left
                
        
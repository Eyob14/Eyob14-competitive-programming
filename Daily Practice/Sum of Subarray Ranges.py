from typing import List
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        
        for i in range(len(nums)):
            current_max = nums[i]
            current_min = nums[i]
            
            for j in range(i, len(nums)):
                current_max = max(current_max, nums[j])
                current_min = min(current_min, nums[j])
                total += (current_max - current_min)
        return total
        
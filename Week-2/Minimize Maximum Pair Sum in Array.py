class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sums = []
        start = 0
        end = len(nums)-1
        while start < end:
            value = nums[start]+nums[end]
            sums.append(value)
            start += 1
            end -= 1
        maximum = sums[0]
        for i in range(1,len(sums)):
            if sums[i] > maximum:
                maximum = sums[i]
        return maximum
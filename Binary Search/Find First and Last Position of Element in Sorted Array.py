class Solution:
    def forwardSearch(self,nums, target):
        best = 0
        left = 0
        right = len(nums) - 1  
        while (left <= right):
            mid = left + (right - left)//2
            if (nums[mid] > target):
                right = mid - 1
            elif (nums[mid] < target):
                left = mid + 1
            else:
                best = mid 
                right = mid - 1 
        return best
    def backwardSearch(self, nums, target):
        best = 0
        left = 0
        right = len(nums) - 1  
        while (left <= right):
            mid = left + (right - left)//2
            if (nums[mid] > target):
                right = mid - 1
            elif (nums[mid] < target):
                left = mid + 1
            else:
                best = mid 
                left = mid + 1 
        return best
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        click = True
        best_1 = self.forwardSearch(nums, target, click)
        best_2 = self.backwardSearch(nums, target)
        if len(nums) == 0 and target:
            return [-1, -1]
        elif len(nums) >= 1 and nums[best_1] == target and nums[best_2] == target:
            return [best_1, best_2]
        return [-1, -1]

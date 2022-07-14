class Solution:
    def compare(self, n):
        return int(n)
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=self.compare)
        return nums[len(nums)-k]
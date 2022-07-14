class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        temp = {}
        result = []
        for i in nums:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1
        for key, element in temp.items():
            if element > (len(nums)//3):
                result.append(key)
        return result

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        result = []
        for i in nums1:
            temp = []
            temp.append(i)
            index = nums2.index(i)
            for j in range(index+1, len(nums2)):
                if nums2[j] > i:
                    temp.append(nums2[j])
            if len(temp) > 1:
                result.append(temp[1])
            else:
                result.append(-1)
        return result
            
        
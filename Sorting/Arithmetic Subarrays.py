class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        new = []
        for i in range(len(r)):
            last = nums[l[i]:(r[i]+1)]
            last.sort()
            value = True
            for j in range(len(last)-1):
                if (last[j+1] - last[j]) != (last[1] - last[0]):
                    value = False
                    break
                else:
                    value = True
            new.append(value)
        return new
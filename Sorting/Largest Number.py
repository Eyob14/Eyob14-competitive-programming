class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        variable = []
        result = ""
        for num in nums:
            while num != 0:
                temp = num % 10
                variable.append(temp)
                num = num // 10
        for i in range(len(variable)):
            for j in range(len(variable)-1):
                if variable[j] < variable[j+1]:
                    variable[j], variable[j+1] = variable[j+1], variable[j]
        for i in variable:
            result += str(i)
        return result
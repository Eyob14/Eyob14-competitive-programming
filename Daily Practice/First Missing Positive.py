class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        new_num = [num for num in nums if num > 0]
        unique = set(new_num)
        
        answer = 1
        
        while True:
            if answer in unique:
                answer += 1
            else:
                break
        return answer
            
                
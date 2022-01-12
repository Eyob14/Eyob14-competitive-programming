class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        temp  = []
        temp.append(0)
        
        for i in range(1,len(temperatures)):
            while len(temp)>0 and temperatures[temp[-1]] < temperatures[i]:
                index = temp.pop()
                answer[index] = i - index
            temp.append(i)   
        return answer
        
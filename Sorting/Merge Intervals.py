class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        index = 0
        for i in range(len(intervals)):
            if i == 0:
                result.append(intervals[i])
            elif result[index][1] >= intervals[i][0]:
                result[index][1] = max(result[index][1], intervals[i][1])
            else:
                result.append(intervals[i])
                index += 1
        return result
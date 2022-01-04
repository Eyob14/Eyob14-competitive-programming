class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        counter = {}
        result = []
        for i in nums:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        x = dict(sorted(counter.items(), key=lambda item: item[1]))
        keys = list(x.keys())
        count = len(keys)-1
        for i in range(k):
            result.append(keys[count])
            count -= 1 
        result.sort()
        return result
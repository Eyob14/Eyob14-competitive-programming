class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        length = len(arr)
        counter = {}
        temp = 0
        result = 0
        for i in arr:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        x = dict(sorted(counter.items(), key=lambda item: item[1]))
        keys = list(x.keys())
        i = len(keys)-1
        while temp < length//2:
            temp += x[keys[i]]
            i -= 1
            result += 1
        return result
        
            
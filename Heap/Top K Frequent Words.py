class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {}
        checker = {}
        for i in words:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
        counter = dict(sorted(counter.items(), key=lambda item: item[1]))
        print(counter)
        key = list(counter.items())
        temp = key[-k:]
        print(temp)
        for i in temp:
            i[0], i[1] = i[1], i[0]
        # temp = [() for i in temp]
        print(temp)
                
            
            
            
            
        return ans
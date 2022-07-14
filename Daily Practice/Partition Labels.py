from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # storing the index and letters in the dictinoary 
        position = {}
        for index , current in enumerate(s): 
            position[current] = index
        
        partition = []
        start = 0 
        end = 0
        for index, current in enumerate(s):
            end = max(end, position[current])
            if end == index:
                partition.append((end + 1) - start)
                start= index + 1
        return partition
        
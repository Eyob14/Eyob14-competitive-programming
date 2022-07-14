class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            first = stones.pop()
            second = stones.pop()
            if first == second:
                stones.append(0)
            else:
                stones.append(first - second)
            stones.sort()
        if stones:
            return stones[0]
        else:
            return 0
# Solution using javascript

/**
 * @param {number[]} stones
 * @return {number}
 */
 var lastStoneWeight = function(stones) {
    stones.sort((a, b) => a-b);
    while (stones.length > 1) {
        first = stones.pop()
        second = stones.pop()
        if (first == second) {
            stones.push(0)
        }
        else {
            stones.push(first - second)
        }
        stones.sort((a, b) => a-b);
    }
    if (stones) {
        return stones[0]
    }
    else {
        return 0
    }
};
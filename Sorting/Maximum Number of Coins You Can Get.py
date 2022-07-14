class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        m = len(piles)-2
        total = 0
        for i in range(len(piles)//3):
            total += piles[m]
            m -= 2
        return total
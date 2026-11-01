import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate, maxRate = math.ceil(sum(piles) / h), max(piles)
        res = maxRate

        while minRate <= maxRate:
            currRate, hours = (minRate + maxRate) // 2, 0
            for p in piles:
                hours += math.ceil(p / currRate)
                if hours > h:
                    minRate = currRate+1
                    break
            if hours <= h:
                res = currRate
                maxRate = currRate-1
        return res
            
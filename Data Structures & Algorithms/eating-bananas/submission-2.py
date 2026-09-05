import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate = max(piles)

        l, r = 1, max(piles)
        mid = (l+r)//2
        while l <= r:
            currHrs = 0
            currRate = mid
            for i in piles:
                currHrs += math.ceil(i/currRate)
            if currHrs <= h:
                r = mid-1
                mid = (l+r)//2
                minRate = min(currRate, minRate)
            else:
                l = mid+1
                mid = (l+r)//2
        return minRate
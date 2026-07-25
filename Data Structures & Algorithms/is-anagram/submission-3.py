class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashX = {}
        hashY = {}

        for x in s:
            hashX[x] = 1 + hashX.get(x, 0)

        for y in t:
            hashY[y] = 1 + hashY.get(y, 0)

        if hashX == hashY:
            return True
        else: return False
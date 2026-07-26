class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = [0] * len(height)
        res = 0

        highest = 0
        for i, n in enumerate(height):
            left.append(highest)
            highest = max(n, highest)

        highest = 0
        for i, n in reversed(list(enumerate(height))):
            right[i] = highest
            highest = max(n, highest)

        for i, n in enumerate(height):
            bottleneck = min(left[i], right[i])
            waterLevel = bottleneck - n
            if waterLevel > 0:
                res += waterLevel
        return res
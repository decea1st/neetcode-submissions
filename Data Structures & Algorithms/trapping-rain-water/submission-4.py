class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        bL = bR = res = 0
        i = 1
        bars = []

        while i < n:
            if height[i-1] > height[i]:
                bL = height[i-1]
                while i < n and height[i] < bL:
                    if (i == n-1 and height[i] > height[i-1]) or i < n-1:
                        bars.append(height[i])
                    i += 1
                    if i < n and height[i] > height[i-1] and height[i] > bR:
                        bR = height[i]
                bottleneck = min(bL, bR)
                if bottleneck != 0:
                    for b in bars:
                        water = bottleneck - b
                        if water >= 0:
                            res += water
                bars = []
                bL = bR = 0
                i += 1
            else:
                i += 1
        return res
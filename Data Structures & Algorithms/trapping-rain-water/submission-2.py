class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [0,2,0,3,1,0,1,3,2,1]
        # go through the array 
        # check if i-1 > i
        # if it is, start of a boundary,
        # keep going till i >= boundary.
        # stop
        # [0], bL = 1, bR = 3
        # heights = [max(bL, bR) - i]
        n = len(height)
        bL = bR = res = 0
        i = 1
        bars = []

        while i < n:
            if height[i-1] > height[i]:
                bL = height[i-1]
                while i < n and height[i] < bL:
                    if i == n-1 and height[i] > height[i-1]:
                        bars.append(height[i])
                    elif i == n-1:
                        break
                    else:
                        bars.append(height[i])
                    i += 1
                    if i < n and height[i] > height[i-1] and height[i] > bR:
                        bR = height[i]
                bottleneck = min(bL, bR)
                print(bars)
                for b in bars:
                    if bottleneck == 0:
                        break
                    water = bottleneck - b
                    if water >= 0:
                        res += water
                bars = []
                bL = bR = 0
                i += 1
            else:
                i += 1
        return res
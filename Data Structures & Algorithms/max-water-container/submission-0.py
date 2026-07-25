class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        n = len(heights)
        l, r = 0, n-1

        while l < r:
            currArea = min(heights[l], heights[r])*(r-l)
            largest = max(currArea, largest)
            if heights[l] < heights[r]: l += 1
            else: r -= 1

        return largest
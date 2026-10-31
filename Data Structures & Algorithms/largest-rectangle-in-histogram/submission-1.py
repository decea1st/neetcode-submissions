class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        heights.append(0) # Needed for cases where it's only ascending numbers
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                if stack: width = i - (stack[-1] + 1)
                else: width = i
                res = max(res, height*width)
            stack.append(i)
        return res
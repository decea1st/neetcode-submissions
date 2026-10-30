class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i, t in enumerate(temperatures):
            while stack:
                if temperatures[stack[-1]] < t:
                    res[stack[-1]] = i-stack[-1]
                    stack.pop()
                else:
                    break
            stack.append(i)
        return res
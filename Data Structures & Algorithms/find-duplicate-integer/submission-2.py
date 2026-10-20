from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        for _ in range(len(nums)+1):
            i = nums[i]
        
        L, j = 1, nums[i]
        while j != i:
            j = nums[j]
            L += 1

        i, j = 0, 0
        for _ in range(L):
            j = nums[j]

        while i != j:
            i, j = nums[i], nums[j]
        
        return i
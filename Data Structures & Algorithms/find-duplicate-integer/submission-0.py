from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for n in freq:
            if freq[n] > 1:
                return n
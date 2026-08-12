class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        tail = 0
        maxLen = currLen = 0

        for i, ch in enumerate(s):
            if ch in seen and seen[ch] >= tail:
                maxLen = max(maxLen, currLen)
                tail = seen[ch]+1
            else:
                currLen = i+1 - tail
            seen[ch] = i
        return max(maxLen, currLen)
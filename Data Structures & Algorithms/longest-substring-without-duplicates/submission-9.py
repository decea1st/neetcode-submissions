class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        tail = 0
        maxLen = currLen = 0

        for i, ch in enumerate(s):
            if ch in seen:
                maxLen = max(maxLen, currLen)
                newTail = seen[ch]+1
                for j in range(tail, i):
                    if s[j] == ch:
                        seen[s[j]] = i
                        break
                    del seen[s[j]]
                tail = newTail
            else:
                seen[ch] = i
                currLen = i+1 - tail
        return max(maxLen, currLen)
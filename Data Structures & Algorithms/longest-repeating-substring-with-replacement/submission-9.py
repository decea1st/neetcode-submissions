class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        for i in range(len(s)):
            counts = {}
            counts[s[i]] = 1
            currLen = 0
            for j in range(1+i, len(s)):
                counts[s[j]] = counts.get(s[j], 0) + 1
                countOfRest = sum(counts.values()) - max(counts.values())
                if len(counts) > 1 and countOfRest > k: break
            
            for key, values in counts.items(): currLen += values
            if countOfRest > k: currLen -= 1
            longest = max(currLen, longest)

        return longest
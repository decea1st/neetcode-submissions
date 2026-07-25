class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        for i in range(len(s)):
            substring = [s[i]]
            counts = {}
            counts[s[i]] = 1
            currLen = 0
            for j in range(1+i, len(s)):
                counts[s[j]] = counts.get(s[j], 0) + 1
                if len(counts) > 1 and (sum(counts.values()) - max(counts.values())) > k:
                    break
            for key, values in counts.items():
                currLen += values

            print(counts)
            if sum(counts.values()) - max(counts.values()) > k: currLen += - 1

            longest = max(currLen, longest)

        return longest

        {A: 4, B: 1}
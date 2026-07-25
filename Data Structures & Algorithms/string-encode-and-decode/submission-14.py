class Solution:
    def encode(self, strs: List[str]) -> str:
        # length of word -> # -> word
        # ex: 4#neet4#code4#love3#you
        return ("".join(f"{len(s)}#{s}" for s in strs))

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            hashIndex = s.find("#", i)
            wordLen = int(s[i:hashIndex])
            start = hashIndex + 1
            end   = start + wordLen
            result.append(s[start:end])
            i = end

        return (result)
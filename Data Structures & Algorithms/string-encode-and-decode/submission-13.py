class Solution:
    def encode(self, strs: List[str]) -> str:
        return ("".join(f"{len(s)}#{s}" for s in strs))

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        i = 0
        while i < len(s):
            hashIndex = s.find("#", i)
            wordLen = int(s[i:hashIndex])
            result.append(s[hashIndex+1:hashIndex+1+wordLen])
            i = hashIndex+wordLen+1

        return (result)
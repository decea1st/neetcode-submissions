class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashB = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in hashB:
                hashB[key] = []
                hashB[key].append(word)
            else:
                hashB[key].append(word)

        result = []
        for keyX in hashB:
            result.append(hashB[keyX])

        return(result)
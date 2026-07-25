class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        used = set()

        for item in range(len(strs)):
            build = []
            if item not in used: build.append(strs[item])

            for rest in range(item + 1, len(strs)):
                checkUsed = (item not in used) and (rest not in used)
                if ( (self.isAnagram(strs[item], strs[rest])) and checkUsed):
                    build.append(strs[rest])
                    used.add(rest)
            used.add(item)
            
            if build: result.append(build)

        return result

    def isAnagram(self, x: str, y: str):
        hashX = {}
        hashY = {}

        for letter in x:
            hashX[letter] = hashX.get(letter, 0) + 1

        for letter in y:
            hashY[letter] = hashY.get(letter, 0) + 1

        if hashX == hashY: return True
        else: return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        hashS, hashT = {}, {}
        # populate a hash map like: a: 1
        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        for x in hashS:
            if hashS[x] != hashT.get(x, 0): return False
        return True
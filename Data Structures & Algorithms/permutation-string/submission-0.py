class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1chars = Counter(s1)
        print(s1chars)

        sub = ""
        for i in range(len(s2)):
            if s2[i] in s1chars:
                sub = s2[i : i+len(s1)]
                hashS = Counter(sub)
                print(hashS)
                if hashS == s1chars:
                    return True

        return False
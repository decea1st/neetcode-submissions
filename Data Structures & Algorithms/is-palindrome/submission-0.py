class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = []
        revLetters = []
        for i in s:
            if i.isalnum():
                letters.append(i.lower())
                revLetters.append(i.lower())
        revLetters.reverse()
        if letters == revLetters: return True
        else: return False
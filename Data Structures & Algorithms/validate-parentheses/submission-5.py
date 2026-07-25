class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        stack = []
        print(stack)
        match = {')' : '(', ']' : '[', '}' : '{'}

        for ch in s:
            if ch in match.values(): stack.append(ch)
            print(stack)
            if ch in match:
                if not stack: return False
                if stack[-1] == match[ch]: stack.pop()
                else: return False
        return not stack
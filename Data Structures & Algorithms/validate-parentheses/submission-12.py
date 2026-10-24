class Solution:
    def isValid(self, s: str) -> bool:
        comp = {  ")": "(", "]" : "[", "}" : "{" }
        openP = set(["(", "[", "{"])
        stack = []

        for p in s:
            if p in openP:
                stack.append(p)
            elif stack and stack[-1] == comp[p]:
                stack.pop()
            else:
                return False
        return not stack
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack = []
        for c in s:
            if c in dic and stack:
                if dic[c] == stack.pop():
                    continue
                else:
                    return False
            stack.append(c)
        return True if not stack else False

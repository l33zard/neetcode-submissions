class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = { ")" : "(",
                "]" : "[",
                "}" : "{"}
        for c in s:
            if stack and c in dic:
                last = stack.pop()
                if dic[c] == last:
                    continue 
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True 

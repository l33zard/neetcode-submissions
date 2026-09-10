class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = { "}" : "{", 
                "]" : "[",
                ")" : "(" }
        for c in s:
            if c in dic and stack:
                popped = stack.pop() 
                if dic[c] == popped:
                    continue 
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True 
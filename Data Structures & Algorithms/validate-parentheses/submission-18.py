class Solution:
    def isValid(self, s: str) -> bool:
        dic = { "}" : "{", 
                "]" : "[",
                ")" : "("}
        stack = []
        for c in s:
            if c in dic and stack:
                popped = stack.pop() 
                if popped != dic[c]:
                    return False 
            else:
                stack.append(c)
        return False if stack else True 
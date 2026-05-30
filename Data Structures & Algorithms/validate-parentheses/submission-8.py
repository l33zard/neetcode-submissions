class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'}':'{', 
                ']':'[',
                ')':'('}
        stack = []
        for char in s:
            if char in dic:
                if stack and dic[char] == stack.pop():
                    continue 
                else:
                    return False
            else:
                stack.append(char)
        return False if stack else True
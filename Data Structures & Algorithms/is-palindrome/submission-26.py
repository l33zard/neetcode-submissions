class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = "" 
        for c in s:
            if self.isalNum(c):
                newStr += c.lower()
        return newStr == newStr[::-1] 

    def isalNum(self, c):
        return (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')) or (ord('0') <= ord(c) <= ord('9'))
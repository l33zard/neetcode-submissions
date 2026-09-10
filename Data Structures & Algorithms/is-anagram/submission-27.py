class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        countS = [0] * 26 
        countT = [0] * 26
        for c in range(len(s)):
            countS[ord(s[c]) - ord('a')] += 1
            countT[ord(t[c]) - ord('a')] += 1
        return countS == countT 
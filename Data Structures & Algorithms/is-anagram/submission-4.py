class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False 
        
        sdic = {}
        tdic = {}

        for i in range(len(s)):
            sdic[s[i]] = 1 + sdic.get(s[i], 0)
            tdic[t[i]] = 1 + tdic.get(t[i], 0)

        return sdic == tdic 
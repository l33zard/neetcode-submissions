class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = {}
        tdic = {}
        for char in s:
            if char in sdic:
                sdic[char] += 1
            else:
                sdic[char] = 1
        
        for char in t:
            if char in tdic:
                tdic[char] += 1
            else:
                tdic[char] = 1
        
        return sdic == tdic 
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
        
        for key in sdic:
            if key not in tdic:
                return False 
            else:
                if sdic[key] != tdic[key]:
                    return False 

        for key in tdic:
            if key not in sdic:
                return False 
            else:
                if sdic[key] != tdic[key]:
                    return False 
        return True 
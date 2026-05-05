class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        hm = {}
        longest = 0 
        r = 0 

        while r < len(s):
            if s[r] in hm:
                l = max(hm[s[r]] + 1, l)
            hm[s[r]] = r
            r += 1
            longest = max(longest, r - l)
        
        return longest
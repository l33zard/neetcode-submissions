class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        hm = {}
        longest = 0 

        for r in range(len(s)):
            if s[r] in hm:
                l = max(hm[s[r]] + 1, l)
            hm[s[r]] = r 
            longest = max(longest, r - l + 1)
        
        return longest
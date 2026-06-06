class Solution:
    def isHappy(self, n: int) -> bool:
        hm = set()
        while n not in hm:
            hm.add(n)
            n = self.sumSq(n)
            if n == 1:
                return True 
        return False
        
    def sumSq(self, n):
        res = 0 
        while n > 0:
            res += (n % 10) ** 2
            n //= 10
        return res
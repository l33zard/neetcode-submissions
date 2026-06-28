class Solution:
    def isHappy(self, n: int) -> bool:
        hm = set()
        while n not in hm:
            hm.add(n) 
            n = self.sq(n) 
            if n == 1:
                return True 
        return False

    
    def sq(self, n):
        res = 0 
        while n:
            res += (n % 10) ** 2
            n //= 10
        return res
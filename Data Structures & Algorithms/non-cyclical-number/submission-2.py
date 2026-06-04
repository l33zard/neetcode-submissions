class Solution:
    def isHappy(self, n: int) -> bool:
        hm = set()
        while n not in hm:
            hm.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True 
        return False
        
    def sumOfSquares(self, n: int) -> int:
        res = 0
        while n > 0:
            res += (n % 10) ** 2
            n //= 10 
        return res

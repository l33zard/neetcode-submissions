class Solution:
    def isHappy(self, n: int) -> bool:
        hm = set()
        while n:
            if n in hm:
                return False 
            hm.add(n)
            n = self.sq(n)
            if n == 1:
                return True 

    
    def sq(self, n):
        res = 0 
        while n:
            res += (n % 10) ** 2
            n //= 10
        return res
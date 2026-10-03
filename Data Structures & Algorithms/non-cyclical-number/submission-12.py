class Solution:
    def isHappy(self, n: int) -> bool:
        dic = set() 
        while n:
            if n in dic:
                return False 
            if n == 1:
                return True 
            dic.add(n) 
            n = self.sq(n)
        return False

    def sq(self, n):
        res = 0 
        while n:
            digit = n % 10 
            res += digit ** 2
            n //= 10 
        return res
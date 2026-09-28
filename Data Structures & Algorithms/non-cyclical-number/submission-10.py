class Solution:
    def isHappy(self, n: int) -> bool:
        dic = set() 
        while n != 1:
            dic.add(n)
            n = self.sq(n) 
            if n in dic:
                return False
            
        return True

    def sq(self, n):
        res = 0 
        while n:
            digit = n % 10
            res += digit ** 2
            n //= 10
        return res
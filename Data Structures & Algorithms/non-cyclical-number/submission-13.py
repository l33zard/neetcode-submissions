class Solution:
    def isHappy(self, n: int) -> bool:
        dic = set() 
        while n != 1:
            if n in dic:
                return False 
            dic.add(n) 
            n = self.sq(n)
        return True 

    def sq(self, n):
        res = 0 
        while n: 
            digit = n % 10 
            res += digit ** 2
            n //= 10 
        return res
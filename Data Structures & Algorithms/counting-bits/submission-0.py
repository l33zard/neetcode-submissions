class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res += [self.noOfOnes(i)]
        return res
    
    def noOfOnes(self, n):
        count = 0
        while n > 0:
            n &= (n - 1)
            count += 1
        return count
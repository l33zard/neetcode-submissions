class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            addbit = (n >> i) & 1
            res |= (addbit << (31 - i))
        return res
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            n ^= nums[i] ^ i
        return n 
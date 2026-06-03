class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        output = 0
        for i in range(0, len(nums)):
            output ^= nums[i] 
        return output
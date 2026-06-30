class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            aim = target - num 
            if aim in dic:
                return [dic[aim], i]
            dic[num] = i
        
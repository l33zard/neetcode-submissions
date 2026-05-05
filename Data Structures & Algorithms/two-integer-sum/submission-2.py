class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list = {}
        for i, num in enumerate(nums):
            aim = target - num 
            if aim in num_list:
                return [num_list[aim], i]
            num_list[num] = i
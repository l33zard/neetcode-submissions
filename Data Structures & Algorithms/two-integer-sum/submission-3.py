class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            partner = target - num
            if partner in dic:
                return [dic[partner], i]
            dic[num] = i
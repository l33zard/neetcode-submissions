class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            tar = target - num 
            if tar in dic:
                return [dic[tar], i]
            dic[num] = i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            t = target - num 
            if t in dic:
                return [dic[t], i]
            dic[num] = i
        
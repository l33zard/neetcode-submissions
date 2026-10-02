class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} 
        for i, num in enumerate(nums):
            n2 = target - num 
            if n2 in dic:
                return [dic[n2], i]
            dic[num] = i
            
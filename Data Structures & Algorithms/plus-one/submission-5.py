class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        if digits[-1] < 9:
            digits[-1] += 1
            return digits 
        else:
            digits = self.plusOne(digits[0: len(digits) - 1])+ [0] 
            return digits
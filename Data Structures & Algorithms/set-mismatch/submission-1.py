class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums) + 1):
            if nums.count(i) == 2:
                a = i
            if i not in set(nums):
                b = i
        
        return [a, b]
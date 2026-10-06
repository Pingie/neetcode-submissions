class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = {}
        for i in range(len(nums)):
            cnt[nums[i]] = cnt.get(nums[i], 0) + 1
            if cnt[nums[i]] == 2:
                a = nums[i]
            if (i + 1) not in set(nums):
                b = i + 1
        
        return [a, b]
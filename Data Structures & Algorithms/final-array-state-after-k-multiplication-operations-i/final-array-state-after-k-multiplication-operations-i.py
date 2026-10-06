class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        n = len(nums)
        while k:
            min_value = 1e18
            for i in range(n):
                if min_value > nums[i]:
                    j = i
                    min_value = min(min_value, nums[i])
            
            nums[j] = min_value * multiplier
            
            k -= 1
        
        return nums
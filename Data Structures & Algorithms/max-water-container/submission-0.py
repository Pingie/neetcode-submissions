class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0
        
        while left < right:
            # Calculate water volume for current pointers
            current_height = min(heights[left], heights[right])
            current_width = right - left
            max_water = max(max_water, current_height * current_width)
            
            # Move the pointer of the shorter bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
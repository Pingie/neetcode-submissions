class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        stack = []

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                bottom = stack.pop()

                if not stack:
                    break

                left = stack[-1]
                right = i

                bounded_height = min(height[left], height[right]) - height[bottom]
                width = right - left - 1

                total_water += bounded_height * width
            
            stack.append(i)


        return total_water

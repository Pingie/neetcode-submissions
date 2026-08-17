class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        L = [-1] * n
        R = [n] * n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                L[i] = stack[-1]
            
            stack.append(i)
        
        while stack:
            stack.pop()

        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                R[i] = stack[-1]

            stack.append(i)

        result = 0
        for i in range(n):
            result = max(result, heights[i] * (R[i] - L[i] - 1))
        
        return result
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            cell_value = matrix[row][col]

            if cell_value == target:
                return True
            
            elif cell_value > target:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return False

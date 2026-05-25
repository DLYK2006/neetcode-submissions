class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            # Map 1D index back to 2D
            val = matrix[mid // n][mid % n]

            if val == target:
                return True
            elif val < target:
                left = mid + 1   # ✅ move forward by 1
            else:
                right = mid - 1  # ✅ move backward by 1

        return False
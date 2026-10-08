class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        # Find the possible row
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        if right == -1:
            return False

        mid = right

        # Binary search inside the row
        left = 0
        right = len(matrix[mid]) - 1

        while left <= right:
            middle = (left + right) // 2

            if matrix[mid][middle] == target:
                return True
            elif matrix[mid][middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False
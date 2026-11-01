class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix)-1, len(matrix[0])-1
        targetRow = -1

        start, end = 0, rows
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                end = mid-1
            if matrix[mid][0] < target:
                if matrix[mid][cols] == target:
                    return True
                elif matrix[mid][cols] > target:
                    targetRow = mid
                    break
                else:
                    start = mid+1

        start, end = 0, cols
        while start <= end and targetRow != -1:
            mid = (start + end) // 2
            if matrix[targetRow][mid] == target:
                return True
            if matrix[targetRow][mid] > target:
                end = mid-1
            if matrix[targetRow][mid] < target:
                start = mid+1
        return False
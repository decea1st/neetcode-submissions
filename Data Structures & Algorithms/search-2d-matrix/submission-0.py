class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find row:
        row = -1
        cols = len(matrix[0])-1
        for r in range(0, len(matrix)):
            start, end = matrix[r][0], matrix[r][cols]
            if start <= target and end >= target:
                row = r
        if row == -1: return False

        l, r = 0, cols
        mid = (l+r)//2
        while l <= r:
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                r = mid-1
                mid = (l+r)//2
            if matrix[row][mid] < target:
                l = mid+1
                mid = (l+r)//2
        return False
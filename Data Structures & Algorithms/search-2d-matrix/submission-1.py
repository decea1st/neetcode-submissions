class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix)-1, len(matrix[0])-1
        # Find row:
        row = -1
        t, b = 0, rows
        mid = (t+b)//2
        while t <= b:
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                b = mid-1
                mid = (t+b)//2
            if matrix[mid][0] < target:
                if matrix[mid][0] <= target and matrix[mid][cols] >= target:
                    row = mid
                    break
                else:
                    t = mid+1
                    mid = (t+b)//2

        if row == -1: return False
        # Search row
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
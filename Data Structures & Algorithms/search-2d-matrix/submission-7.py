class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix) # row count
        n = len(matrix[0]) # column count
        t = m * n  # Total elements in 2D matrix
        l = 0
        r = t - 1
        while l <= r:
            mid = (l + r) // 2
            i = mid // n
            j = mid % n
            mid_num = matrix[i][j]
            if target > mid_num:
                l = mid + 1
            elif target < mid_num:
                r = mid - 1
            else:
                return True
        return False

                
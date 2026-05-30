class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
             for j in range(len(matrix) + 1):
                #print(matrix[i][j])
                if matrix[i][j] == target:
                    return True
        return False
        
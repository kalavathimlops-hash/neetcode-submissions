class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        for i in range(len(matrix)):
             for j in range(len(matrix[i])):
                #print(matrix[i][j])
                if matrix[i][j] == target:
                    return True
        return False
        
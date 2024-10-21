"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/set-matrix-zeroes/description/?envType=problem-list-v2&envId=hash-table
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()
        zero_cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for i in zero_rows:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0 
        for i in zero_cols:
            for j in range(len(matrix)):
                matrix[j][i] = 0

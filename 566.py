'''
In MATLAB, there is a very useful function called 'reshape', 
which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, 
and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, 
output the new reshaped matrix; Otherwise, output the original matrix.
'''


class Solution:
    def matrixReshape(self, nums: list, r: int, c: int):
        a = len(nums)
        b = len(nums[0])
        matrix = []
        if a*b == r*c:
            for i in range(0, a):
                for j in range(0, b):
                    matrix.append(nums[i][j])

            matrixNew = []
            count = 0
            for i in range(0, r):
                matrix_ = []
                for j in range(0, c):
                    matrix_.append(matrix[count])
                    count += 1
                matrixNew.append(matrix_)
        
            return matrixNew

        if a*b != r*c:
            return nums
        
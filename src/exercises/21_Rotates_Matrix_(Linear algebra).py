"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Rotates the matrix according the desired output.
        """

        # To accomplish the desired output, it is needed to first:
        # 1. Transpose the matrix, 2. Reflect the matrix.
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix:list) -> None:
        """
        Transform the matrix by flipping the elements over matrix diagonal.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):  
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


    def reflect(self, matrix:list) -> None:
        """
        Transform the matrix by reversing each vector elements.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]



if __name__ == "__main__":
    sol = Solution()
    matrix:list = [[1,2,3],[4,5,6],[7,8,9]]
    # Output must be: [[7,4,1],[8,5,2],[9,6,3]]

    print(sol.rotate(matrix=matrix))

    print(matrix)
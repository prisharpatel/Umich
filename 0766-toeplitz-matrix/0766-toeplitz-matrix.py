class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # go through diagonals from top left to bottom right and see if numbers ar ethe same 
        # if not, return false 

        m = len(matrix)
        n = len(matrix[0])

        diagonals = m + n - 1

        for i in range(n-1, -1, -1):
            # check diagonals starting in first row from right side
            # going down , so increase row and increase column
            row = 0 
            col = i
            value = matrix[row][col]
            while (col + 1 < n and row +1 < m):
                col += 1
                row += 1
                if matrix[row][col] != value:
                    return False
        
        for i in range(1, m):
            # check diagonals starting in first column
            row = i 
            col = 0
            value = matrix[row][col]
            while (col + 1 < n and row +1 < m):
                col += 1
                row += 1
                if matrix[row][col] != value:
                    return False


        return True
             




        
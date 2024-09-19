class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # go through matrix on diagonals 
        # matrix traversal/arrays problem 
        m = len(mat)
        n = len(mat[0])

        sol = []

        row = 0 
        col = 0
        up = True
        # iterate over diagonals
        while len(sol) < m *n:
            # print("row: ", row)
            # print("col: ", col)
            sol.append(mat[row][col]) # add head of diagonal
            if up: # going up diagonal
                # subtract row, add column 
                while col +1 < n and row-1 >= 0:
                    sol.append(mat[row-1][col+1])
                    row -= 1
                    col += 1
                if col != (n-1):
                    col += 1
                else: 
                    row += 1
                
                up = False
            else:
                # add row, subtract column
                while col-1 >= 0 and row+1 < m:
                    sol.append(mat[row+1][col-1])
                    row += 1
                    col -= 1
                up = True
                if col != 0 or row + 1 == m:
                    col += 1
                else:
                    row += 1
                
                
            # print(sol)
        return sol

        

        
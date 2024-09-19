class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # go through all values in the matrix: O(m*n) and return them in spiral order
        # matching - array, matrix problem 
        output = []
        # pattern: going out to in taking top row, right column, bottom row, left column

        # pseudocode:
        
        elementsFound = 0
        elementsNeeded = len(matrix) * len(matrix[0])

        while (elementsFound < elementsNeeded):
            rows = len(matrix)
            cols = len(matrix[0])

            # get top row
            output += matrix[0]
            
            if cols-1 != 0:
                # get last column
                for i in range(1, rows-1):
                        output.append(matrix[i][cols-1])
                        matrix[i].pop(cols-1)

                # get bottom row
                if rows-1 != 0:
                    row = matrix[rows-1]
                    row.reverse()
                    output += row
                # output.append(matrix[rows-1][::-1])

                # get first column
                for i in range(rows-2, 0, -1):
                    if len(matrix[i]) > 0:
                        output.append(matrix[i][0])
                        matrix[i].pop(0)

                matrix.pop(rows-1)
            
            if matrix:
                matrix.pop(0)
            elementsFound = len(output)
            
        return output



        
        
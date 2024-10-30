class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # understand 
        # determine if a sudoku board is valid - only filled cells need to be validated so 
        # if its empty, ignore  
        # return true or false

        # matching - matrix, array 

        # pseudocode
        # go through rows 
        for row in board: 
            exists = set()
            for element in row: 
                if element in exists: 
                    return False 
                elif element != ".":
                    exists.add(element)

        # go through columns 

        for c in range(9): 
            exists = set()
            for r in range(9): 
                if board[r][c] in exists: 
                    return False
                elif board[r][c] != ".":
                    exists.add(board[r][c])

        # go through 3x3 grids 
        for start_r in range(0, 9, 3): 
            for start_c in range(0, 9, 3): 
                exists = set()
                for r in range(start_r, start_r+3):
                    for c in range(start_c, start_c+3): 
                        if board[r][c] in exists: 
                            return False
                        elif board[r][c] != ".": 
                            exists.add(board[r][c])
                        

        return True # made it through all checks 
        
        # time complexity: O(1) bc all boards will be of length 9


        
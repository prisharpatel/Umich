class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # output a matrix that represents what happens to stones once the box is rotated 90 degrees

        # first rotate the box 90 degrees
        # all rows become columns with top row being left most column = transpose of matrix and reverse rows
        rows = len(box)
        cols = len(box[0])
        newBox = [[0] * rows for _ in range(cols)]


        for r in range(len(box)):
            for c in range(len(box[r])):
                newBox[c][r] = box[r][c] 

        # go through the box cell by cell to determine if something needs to be changed 
        # stone = # (check whats below it)
        # obstacle = * (skip these)
        # empty = . (skip these)
        for i in range(len(newBox)):
            newBox[i] = list(reversed(newBox[i]))
        

        

        for r in range(len(newBox)):
            for c in range(len(newBox[r])):
                if newBox[r][c] == '#': # found a stone
                    # r is the top pointer and we need to find the bottom pointer which will exist either at
                    # an obstacle or the bottom 
                    # count how many stones u have along the way 
                    check_row = r
                    stones = 0
                    while check_row < len(newBox):
                        if newBox[check_row][c] == '*':
                            break
                        if newBox[check_row][c] == '#':
                            stones += 1
                            newBox[check_row][c] = '.'
                        check_row += 1

                    while stones > 0:
                        stones -=1 
                        newBox[check_row-1][c] = '#'
                        check_row -= 1
                        
        return newBox







        
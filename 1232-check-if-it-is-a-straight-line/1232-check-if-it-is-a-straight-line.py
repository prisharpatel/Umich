class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # check if points make a straight line 
        # which has to be checked using the slope of the line and making sure 
        # each pair of points matches a slope? 

        # take the first two in the list and make that the slope 
        # check every element and compare it with teh first element once simplified to ensure 
        # it has that slope 

        # guaranteed to have two elements so rise over run


        rise = (coordinates[0][1] - coordinates[1][1]) 
        run = (coordinates[0][0] - coordinates[1][0])


        for i in range(2, len(coordinates)):
            checkRise = (coordinates[0][1] - coordinates[i][1]) 
            checkRun = (coordinates[0][0] - coordinates[i][0])
            if rise * checkRun != run * checkRise: # avoids divide by 0 error and creates ratio
                return False
        return True
        
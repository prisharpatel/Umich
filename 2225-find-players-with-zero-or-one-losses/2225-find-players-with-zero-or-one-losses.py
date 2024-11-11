class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # matches[0] = winner
        # matches[1] = loser 


        # answer[0] = no matches lost 
        # answer[1] = lost one match 

        # keep as sets and then convert them into lists

        # matching - array problem, sets
        won = set() # add here when they win and if they lose 
        lostMultiple = set() # losingMorethanOne
        lostOne = set() # lost one match - so if they are in this already when they lose --> remove
    
        for match in matches: 
            winner = match[0]
            loser = match[1]

            # add winner if it isn't in lostOne or lostMultiple 
            if winner not in lostMultiple and winner not in lostOne: 
                won.add(winner)
            
            # loser - add to add one if its not there 
            if loser in lostOne:
                lostOne.remove(loser)
                lostMultiple.add(loser)
            elif loser not in lostMultiple: 
                lostOne.add(loser)
                won.discard(loser) 
             
                
        return [sorted(won), sorted(lostOne)]
            


        
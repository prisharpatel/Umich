from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # matches[0] = winner
        # matches[1] = loser 

        # answer[0] = no matches lost 
        # answer[1] = lost one match 

        # keep as sets and then convert them into lists

        # matching - array problem, sets
        won = set()  # add here when they win and if they lose 
        lostAlready = set()  # track players who have lost more than once
        lostOne = set()  # track players who lost exactly one match
    
        for match in matches: 
            winner = match[0]
            loser = match[1]

            if winner not in lostAlready and winner not in lostOne: 
                # add winner to won set
                won.add(winner)

            if loser in lostOne:
                # move loser from lostOne to lostAlready if this is their second loss
                lostOne.remove(loser)
                lostAlready.add(loser)
            elif loser not in lostAlready:
                # add loser to lostOne if it's their first loss
                lostOne.add(loser)
                # remove loser from won set if they were previously a winner
                won.discard(loser)
        
        # Convert sets to sorted lists for the final answer
        return [sorted(won), sorted(lostOne)]

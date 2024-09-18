class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # merge intervals based on which ones will be within each other
        # sort based on the first element of each of the elements in intervals and merge if 
        # the next one you want to merge with is within it or to the right of it on number line, else add it 
        # to output 

        # sort with lambda
        intervals = sorted(intervals, key=lambda x: x[0])
        
        # for loop to go through intervals and check conditions above 
        output = []
        current = []
        for interval in intervals: 
            if len(output) == 0:
                output.append(interval)
                current = interval
            else:
                # check if you can merge
                # within 
                if interval[0] >= current[0] and interval[1] <= current[1]:
                    continue # don't need to add to output since within another interval already
                # to teh right
                if interval[0] >= current[0] and interval[1] >= current[1] and interval[0] <= current[1]:
                    output.remove(current)
                    current = [current[0], interval[1]]
                    output.append(current)
                    continue
                # nothing 
                output.append(interval)
                current = interval
        return output
                

    
        
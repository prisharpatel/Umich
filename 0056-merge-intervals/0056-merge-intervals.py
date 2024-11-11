class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by the first time 
        # check two things 
            # is the interval within the current interval we are looking at
            # can the interval extend the current interval we are looking at

        # can sort in place
        intervals.sort(key = lambda x: x[0])
        current = intervals[0] # guaranteed to have length of 1
        # go through itnervals and check above two checks 
        merged = []
        for interval in intervals:
            left = interval[0]
            right = interval[1]
            if left >= current[0] and right <= current[1]: 
                # fits inside current interval, so move on
                continue 
            elif  current[0] <= left <= current[1] and right > current[1]: 
                current[1] = right
                continue 
                # extends interval
            else: 
                merged.append(current)
                current = interval
        merged.append(current)
        return merged
        
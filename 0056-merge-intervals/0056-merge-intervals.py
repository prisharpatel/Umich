class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals
        # intervals[i] = [start, end]

        # return array of non-overlapping intervals 

        # matching - sorting, array
        if intervals is None:
            return intervals

        # pseduo 1) sort array by the start element
        intervals = sorted(intervals, key = lambda x: x[0])
        # have output array 
        output = []
        # go through sorted array and extend what is in the output array if following conditions are met
            # adding start < end in array 
        # else: 
            # add something new to output 
        for interval in intervals:
            if output == []: 
                output.append(interval)
                continue
            if output[-1][1] >= interval[0] and interval[1] > output[-1][1]:
                # extend output 
                output[-1][1] = interval[1]
            if interval[0] >= output[-1][0] and interval[1] <= output[-1][1]:
                continue # don't do anything because adding interval is within the one that exists already...
            else:
                output.append(interval)             
        return output
        # 
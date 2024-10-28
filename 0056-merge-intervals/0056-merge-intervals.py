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
            if output[-1][1] >= interval[0]:
                # extend output 
                output[-1][1] = interval[1]
            else:
                output.append(interval)             
        return output
        # 
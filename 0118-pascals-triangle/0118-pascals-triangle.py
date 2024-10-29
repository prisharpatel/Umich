class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # return first numRows of pascals triangle 

        # matching - math, arrays 

        # pseudocode:
        output = [[1]]
        

        for num in range(1, numRows):
            
            last_row = output[-1]
            cur_row = [last_row[0]]
            i =0 
            while i < len(last_row) - 1:
                
                cur_row.append(last_row[i] + last_row[i+1])
                i += 1
            # add last value
            cur_row.append(output[-1][-1])
            output.append(cur_row)


        return output

        
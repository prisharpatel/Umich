class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # brute force
        # try to build the soluition and check if numbers u want exist
        
        # decrease count when you use it
        
        # checking if pairs of numbers exist for some i such that 
        
        # pair is such 
        # i = 0: arr[1] = 2 * arr[0]
        # i - 1: arr[3] = 2 * arr[2]
        # i = 2: arr[5] = 2 * arr[4]

        # so we need to ensure that there are len(arr)//2 pairs of numbers that is 2x th eother

        count = Counter(arr)       # decrease x and 2x when its true that the two are there 

        sortArr = sorted(arr, key = abs) # O(nlogn) --> need to sort so that you don't return false too early
        for num in sortArr:
            if count[num] == 0: # already found its pair
                continue
            if count[2*num]== 0:
                return False
            count[num] -= 1
            count[2*num] -= 1
        
        return True
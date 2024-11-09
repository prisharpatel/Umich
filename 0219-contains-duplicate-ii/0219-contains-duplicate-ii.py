class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # double for loop? 
        if len(set(nums)) == len(nums):
            # no duplicates
            return False

        # use a hashmap to check if eleemnt exists and what index it is at if so 
        tracker = set() 
        
        for i in range(len(nums)):
            if nums[i] in tracker: 
                return True
            tracker.add(nums[i])
            if len(tracker) > k: 
                tracker.remove(nums[i-k])
            

        return False        
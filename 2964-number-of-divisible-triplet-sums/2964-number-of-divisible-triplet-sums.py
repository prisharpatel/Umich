class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        n = len(nums)
        count = 0
        pair_mod_count = defaultdict(int)  # Hashmap to store counts of pairs with specific mods

        # Iterate over each element as the third element of the triplet
        for k in range(1, n):
            # Calculate target mod that would make the triplet sum % d == 0
            target_mod = (d - nums[k]) % d
            # Add the count of pairs with the required mod
            count += pair_mod_count[target_mod]

            # Update the pair_mod_count with new pairs that include nums[k-1]
            for j in range(k):
                # Calculate the sum of nums[j] and nums[k-1] % d
                pair_sum_mod = (nums[j] + nums[k]) % d
                pair_mod_count[pair_sum_mod] += 1

        return count


        
        
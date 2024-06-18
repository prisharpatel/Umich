class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0 
        r = len(height) - 1
        max_water = 0
        while (l < r):
            w = r - l
            h = min(height[l], height[r])
            area = w * h
            if area > max_water:
                max_water = area

            if height[l] > height[r]: # move pointer to find a bar that is taller
                r -= 1
            else: 
                l += 1
            
        return max_water



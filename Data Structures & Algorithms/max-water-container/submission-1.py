class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0, len(height) - 1
        maxArea = 0

        while l< r:
            area = (r-l) * min(height[l], height[r])
            maxArea = max(maxArea, area)
            if height[l]< height[r]:
                l +=1
            else:
                r -= 1
        return maxArea

#Time Complexity : O(n)
#Space Complexity: O(1)

"""
#BRUTE FORCE
        res = 0

        for l in range(len(height)):
            for  r in range(l+1, len(height)):
                area = min(height[l], height[r]) * (r -  l)
                res = max(res, area)
        return res

        #Time complexity: O(n^2)
        #Space Complexity: O(1)
        """
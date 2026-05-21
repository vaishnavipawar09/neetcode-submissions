class Solution:
    def rotate(self, nums : List[int], k : int) -> None:
        k = k % len(nums)       #k value to exceed the len of nums

        #Step 1: Reverse the whole array 
        l = 0
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        #Step 2: Reverse upto k
        l = 0
        r = k - 1
        while l< r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        #Step 3: Reverse the remaining array
        l = k
        r = len(nums) - 1
        while l< r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

#Dry Run: nums = 

        
        
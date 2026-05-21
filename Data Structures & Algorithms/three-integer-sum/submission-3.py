class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        i = 0
        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i-1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                calsum = nums[i] + nums[j] + nums[k]
                if calsum > 0:
                    k -= 1
                elif calsum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j -1]:
                        j +=1
        return res

#Time Complexity: O(n^2)    (one loop takes nlog n and the other j, k loop takes n^2 so total it is n^2)
#Space Complexity: O(1) or O(n) depends upon sorting algorithm

    

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map ={}                           #Create a HashMap to store the values
        
        for i, n in enumerate(nums):
            diff = target - n               #To check if the diff exits in hashmap
            if diff in h_map:               #If yes than return index
                return [h_map[diff], i]
            h_map[n] = i                    #Store the value in the hashmap
        return 0
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}                                  #Create a Hashmap
        freq = [[] for i in range(len(nums)+1)]     #Lit of values that occur (Frequency) (Bucket SOrt setup)
                                                    #Need len(nums)+1 buckets cause max freq of any num = len(nums)

        for n in nums:
            count[n] = 1+ count.get(n, 0)           #Append in the Hashmap
        for n, c in count.items():                  #Return the key value pair 
            freq[c].append(n)                       #Fill the bucket
                                                    #For each number and its count, put it in the freq[count] bucket.
        

        res=[]
        for i in range(len(freq) - 1, 0, -1):       #Iterate in Descending order
            for n in freq[i]:
                res.append(n)                       #Keep collecting until you have k elements
                if len(res) == k:                   #Check if k is satisfied
                    return res
        
        
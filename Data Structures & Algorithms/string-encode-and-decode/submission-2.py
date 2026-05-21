class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""                            #Create a single string
        for s in strs:                      #Loop through all the strings
            res += str(len(s)) + "#" + s    #Add strs by the strlen#string format
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0                      #List of strings, create a pointer

        while i < len(s):
            j = i
            while s[j] != "#":            # j is at the delimeter
                j += 1
            length = int(s[i:j])          #convert to int, will tell how many charcters to read after #
            res. append(s[j + 1 : j + 1 + length])
            i = j + 1 + length              #beginning of next string
        return res  

#Time : O(m) for each encode and decode
# Space: O(m +n) for each encode and decode, m = sum of len of all strings, n = numbr of strings

#Pattern: Length-Prefix Encoding (Serialization Pattern)
# Used in: 1.Network protocols
# 2. TCP message framing
# 3. File formats
# 4. Binary encoding

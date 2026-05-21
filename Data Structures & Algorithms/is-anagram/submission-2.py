class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = dict()
        for i in s:
            if i in hashmap:
                hashmap[i] = hashmap[i] + 1
            else:
                hashmap[i] = 1
      
        for j in t:
            if j in hashmap:
                hashmap[j] = hashmap[j] - 1
                if hashmap[j] < 0:
                    return False
            else:
                return False
        return True


        
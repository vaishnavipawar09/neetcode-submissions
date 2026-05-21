# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []                    #Empty string

        def dfs(node):              #Helper function
            if not node:            #if node is null
                res.append("N")     #Append a N char 
                return
            res.append(str(node.val)) #Append the vale to the res
            dfs(node.left)              #traverse on left subtree
            dfs(node.right)             #traverse on right subtree

        dfs(root)                       #pass the root val
        return ",".join(res)            #Join by the , delimeter
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")          #split by the , (comma) delimeter
        self.i = 0                      #a ptr global

        def dfs():                      #helper funt for recursion 
            if vals[self.i] == "N":     #if N return the Null node
                self.i += 1             #icrement i so next val will be there
                return None
            node = TreeNode(int(vals[self.i]))  #conert to int and then pass the value
            self.i += 1                 #increment i to move to next
            node.left = dfs()           #left subtree
            node.right = dfs()          #right subtree
            return node                 #return the root node of the tree

        return dfs()                    #call dfs and return the tree
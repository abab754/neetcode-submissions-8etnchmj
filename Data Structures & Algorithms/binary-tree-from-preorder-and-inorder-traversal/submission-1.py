# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm = {}
        for i in range(len(inorder)):
            hm[inorder[i]] = i
        self.i = 0
        def dfs(l, r):
            if l> r:
                return None
            val = preorder[self.i]
            self.i+=1
            root = TreeNode(val)
            m = hm[val]
            root.left = dfs(l, m-1)
            root.right = dfs(m+1, r)
            return root
        return dfs(0, len(preorder)-1)
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = [root.val]
        def dfs(root):
            if not root:
                return 0

            res = root.val
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)
            ret[0] = max(ret[0], res+left+right)
            return res + max(left, right)
        
        dfs(root)
        return ret[0]
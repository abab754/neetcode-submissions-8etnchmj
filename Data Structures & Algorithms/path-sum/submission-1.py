# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, cur):
            if not root:
                return False
            if not root.left and not root.right:
                return cur + root.val == targetSum
            return dfs(root.left, cur+root.val) or dfs(root.right, cur+root.val)
        
        return dfs(root, 0)
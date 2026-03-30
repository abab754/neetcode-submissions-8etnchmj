# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(root, val):
            cur = 0
            if not root:
                return cur
            if root.val >= val:
                cur = 1
            return cur + dfs(root.left, max(root.val, val)) + dfs(root.right, max(root.val, val))
        
        
        
        return dfs(root, root.val)
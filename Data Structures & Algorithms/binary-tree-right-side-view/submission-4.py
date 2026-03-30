# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            l = len(q)
            for i in range(l):
                popped = q.popleft()
                if i == l-1:
                    res.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
        
        return res
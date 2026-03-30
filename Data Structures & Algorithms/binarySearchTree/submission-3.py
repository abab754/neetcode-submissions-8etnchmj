class TreeNode:
        def __init__(self,key, val, left=None, right=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right
class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        self.root = self.helpInsert(self.root, key, val)

    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if cur.key < key:
                cur = cur.right
            elif cur.key > key:
                cur = cur.left
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.val


    def getMax(self) -> int:
        if not self.root:
            return -1
        cur = self.root
        while cur.right:
            if not cur:
                return -1
            cur = cur.right
        return cur.val

    def remove(self, key: int) -> None:
        self.root = self.helpRemove(self.root, key)

    def getInorderKeys(self) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return res
            if root.left:
                dfs(root.left)
            res.append(root.key)
            if root.right:
                dfs(root.right)
        dfs(self.root)
        return res

    def helpInsert(self, root, key, val):
        if not root:
            return TreeNode(key, val)
        if root.key < key:
            root.right = self.helpInsert(root.right, key, val)
        elif root.key > key:
            root.left = self.helpInsert(root.left, key, val)
        else:
            root.val = val
        return root
    
    def helpRemove(self, root, key):
        if not root:
            return root
        if root.key < key:
            root.right = self.helpRemove(root.right, key)
        elif root.key > key:
            root.left = self.helpRemove(root.left, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            cur = root.right
            while cur.left:
                cur = cur.left
            root.key = cur.key
            root.val = cur.val
            root.right = self.helpRemove(root.right, root.key)
        return root



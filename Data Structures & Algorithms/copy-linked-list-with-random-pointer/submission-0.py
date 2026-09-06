"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {}
        cur = head
        while cur:
            copy = Node(cur.val)
            hm[cur] = copy
            cur = cur.next
        
        cur = head
        dummy = Node(101)
        ptr2 = dummy

        while cur:
            copy = hm[cur]
            ptr2.next = copy
            copy.next = hm[cur.next] if cur.next else None
            copy.random = hm[cur.random] if cur.random else None
            ptr2 = ptr2.next
            cur = cur.next
        
        return dummy.next
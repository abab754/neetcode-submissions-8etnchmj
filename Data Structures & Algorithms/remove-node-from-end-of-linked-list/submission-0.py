# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        size = 0
        while cur.next:
            size+=1
            cur = cur.next
        cur = dummy
        for _ in range(size - n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
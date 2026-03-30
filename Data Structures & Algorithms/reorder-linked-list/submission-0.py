# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        dummy.next = head
        p = dummy

        slow = dummy
        fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow.next
        after = cur
        while cur:
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after
        slow.next = None
        cur = head
        p1 = cur
        p2 = prev
        while p1 and p2:
            p1 = cur.next
            cur.next = p2
            cur = p1
            p2 = prev.next
            prev.next = p1
            prev = p2
        
        

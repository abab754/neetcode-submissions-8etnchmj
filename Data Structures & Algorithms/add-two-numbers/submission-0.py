# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        cur = l1
        while cur:
            num1 += str(cur.val)
            cur = cur.next
        
        num2 = ''
        cur = l2
        while cur:
            num2 += str(cur.val)
            cur = cur.next
        
        num1 = int(num1[::-1])
        num2 = int(num2[::-1])

        res = str(num1 + num2)[::-1]

        dummy = ListNode()
        cur = dummy
        for c in res:
            node = ListNode(int(c))
            cur.next = node
            cur = cur.next
        
        return dummy.next
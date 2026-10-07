# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            p1 = l1
            p2 = l2
            dummy = ListNode()
            cur = dummy
            while p1 and p2:
                if p1.val <= p2.val:
                    cur.next = p1
                    p1=p1.next
                else:
                    cur.next =p2
                    p2=p2.next
                cur=cur.next
            
            while p1:
                cur.next = p1
                p1=p1.next
                cur = cur.next
            
            while p2:
                cur.next = p2
                p2=p2.next
                cur = cur.next

            return dummy.next
        
        q = deque(lists)
        while len(q) >=2:
            l1 = q.popleft()
            l2 = q.popleft()
            new_list = merge(l1, l2)
            q.append(new_list)
        
        return q[0] if len(q) == 1 else None
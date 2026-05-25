# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if cur is None:
            return 
        prev= None
        
        while cur is not None:
            next_node = cur.next
            #flip the pointer
            cur.next = prev # initially None
            prev = cur 
            # cur = cur.next # this would make prev as cur (which is None )
            cur = next_node
        head = prev
        return prev

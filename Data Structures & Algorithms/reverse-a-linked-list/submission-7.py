# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        # next node 
        # flip 
        # point prev
        # move cur next
        while cur is not None:
            next_n = cur.next
            cur.next = prev #flip
            prev = cur
            cur = next_n

        head = prev
        return head

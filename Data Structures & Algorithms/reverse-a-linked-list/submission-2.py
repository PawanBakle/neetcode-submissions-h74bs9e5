# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur is not None:
            # save the next node
            next_node = cur.next
            # flip the direction
            cur.next = prev
            # save the previous node
            prev = cur
            # hop on to next
            cur = next_node
        head = prev
        return head

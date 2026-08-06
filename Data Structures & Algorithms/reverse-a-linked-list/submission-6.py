# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur is not None:
            next_node = cur.next #new node
            #flip
            cur.next = prev
            # add prev
            prev = cur
            # shift
            cur = next_node

        return prev
        
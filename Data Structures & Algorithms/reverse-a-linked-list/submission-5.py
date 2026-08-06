# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        in order to reverse a LL 
        i need a pointer to remember previous Node
        and curr which keeps moving forward and changes direction
        at the same time
        new-node to not loose next Node
        '''
        prev = None
        cur = head
        while cur is not None:
            next_node = cur.next # be connected to new Node
            cur.next = prev # flip the direction
            prev = cur # update previous pointer
            cur = next_node # move cur to next Node

        # cur.next = prev
        # prev = head
        return prev




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur is not None:
            count+=1
            cur = cur.next

        diff = count - n
        if diff == 0:
            return head.next
        target_in = 0
        prev = None
        cur = head
        while target_in != diff:
            target_in += 1
            prev = cur
            cur = cur.next
        # if prev is None:
        #     return cur  
        prev.next = cur.next
        return head
        


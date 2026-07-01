# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = new_ll = ListNode(0)
        cur = new_ll 
        old_ll = head
        while head is not None:
            if head.val == val:
                head = head.next
                continue
                
            
            cur.next = head
            head = head.next
            cur = cur.next
        if cur is not None:
            cur.next = None
        return new_ll.next
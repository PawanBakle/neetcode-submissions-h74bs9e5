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

        total_len = count - n
        if total_len == 0:
            return head.next
        del_count = 0
        prev = None
        cur = head
        while del_count != total_len:
            del_count += 1
            prev = cur
            cur = cur.next
        # if prev is None:
        #     return cur  
        prev.next = cur.next
        return head
        


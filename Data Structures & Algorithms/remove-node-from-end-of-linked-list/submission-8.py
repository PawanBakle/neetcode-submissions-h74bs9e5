# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        val =0
        while val != n:
            if fast.next is not None:
                fast = fast.next
                val +=1
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            # cur.next = prev   

        slow.next = slow.next.next
        return dummy.next


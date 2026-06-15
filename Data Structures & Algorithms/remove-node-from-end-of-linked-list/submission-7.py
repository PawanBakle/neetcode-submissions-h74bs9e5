
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = slow = head
        cur = head
        prev = None
        val = 1
        # if n == 1:
        #     return None
        while val != n:
            if fast.next is not None:
                fast = fast.next
                val +=1
        while fast.next is not None:
            slow = slow.next
            # cur.next = prev
            prev = cur
            cur = cur.next
            fast = fast.next

        # since if slow is still head when fast has reached None
        # means n is actually Head
        if slow == head:
            return slow.next
        prev.next = cur.next
        return head
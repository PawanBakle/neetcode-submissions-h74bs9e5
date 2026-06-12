# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast is not None and fast.next is not None:
            if fast is None or fast.next is None:
                return False
            else:

                slow = slow.next
                fast = fast.next.next
                # eventually they catch up as fast is running
                # as twice as slow
                if slow == fast:
                    return True
        return False
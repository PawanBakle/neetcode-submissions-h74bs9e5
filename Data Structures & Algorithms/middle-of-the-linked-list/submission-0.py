# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        slow, fast = head, head
        while fast and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
        # if not fast.next.next:
        #     return slow.next
        return slow
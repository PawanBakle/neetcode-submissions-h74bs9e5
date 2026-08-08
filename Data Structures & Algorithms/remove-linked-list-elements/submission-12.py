# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        head = new_node = ListNode(None)
        # cur = head
        while cur is not None:
            if cur.val == val:
                cur = cur.next
                continue

            else:
                new_node.next = cur
                new_node = new_node.next
                cur = cur.next
        if new_node.next and new_node.next.val == val:
            new_node.next = None
        return head.next



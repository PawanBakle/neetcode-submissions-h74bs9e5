# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        cur = dummy
        pointer = head
        while pointer is not None:
            if pointer.val == val:
                pointer = pointer.next
            else:
                cur.next = pointer
                cur = cur.next
                pointer = pointer.next
        cur.next = None
        return dummy.next


        # cur = head
        # prev = None
        # if head == val:
        #     cur = head.next
        #     prev = cur

        #     cur = cur.next
        # while cur.next is not None:
        #     while cur != val:
        #         if cur is not None:
        #             prev = cur
        #             cur = cur.next
        #         return cur
        #     prev.next = cur.next
        # return prev






        
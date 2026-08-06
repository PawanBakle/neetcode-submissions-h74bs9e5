# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_ll = ListNode(0)
        head = new_ll
        ll1 = list1
        ll2 = list2 

        while ll1 is not None and ll2 is not None:
            if ll1.val < ll2.val:
                # attach the node to the new LL's next (which is None right now)
                new_ll.next = ll1
                ll1 = ll1.next
                new_ll = new_ll.next
            elif ll2.val < ll1.val:
                # attach the node to the new LL's next (which is None right now)
                new_ll.next = ll2
                ll2 = ll2.next
                new_ll = new_ll.next
            elif ll1.val == ll2.val:
                new_ll.next = ll1
                ll1 = ll1.next
                new_ll = new_ll.next

        if ll2 is not None:
            new_ll.next = ll2
        else:
            new_ll.next = ll1
        return head.next


            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        i am suppose to find all target nodes and update prev 
        and next pointers.
        i need both remember previous and current Node
        
        using a new Dummy LL would help me because here
        i am just adding valid Nodes and not invalid Nodes
        '''
        dummy = ListNode(0)
        prev = None
        pointer = dummy
        cur = head
        # if head = val:
        #     dummpy = head.next
        #     prev = head
        #     cur = cur.next
        while cur is not None:
            if cur.val == val:
                cur = cur.next
            else:
                dummy.next = cur
                cur = cur.next
                dummy = dummy.next
        while dummy is not None:
            if dummy.val == val:
                # prev = dummy
                prev.next = dummy.next
                dummy = dummy.next
            else:
                prev = dummy
                dummy = dummy.next
        # if dummy.next == val:
        #     dummy.next = None
        return pointer.next



        
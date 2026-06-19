# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        unoptimized solution with a lot 
        of repetitions
        and mistakes 
        mistake 1: i was changing variables to different LL and 
        guessing why 2 variables pointing to same LL returned different LL
        (i changed second variable to point to different LL so obv)

        then after a while i figured out that i was suppose to navigate using LL's next pointer
        to keep the variable attached to original LL

        mistake 2: wrong way of navigating the pointers
        and not having concrete reason of how do i attach head to original LL
        '''


        dummy = ListNode(0)
        head = dummy
        # head = dummy
        if list1 is None and list2 is None:
            return None
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:

                dummy.next = list1
                # head = dummy
                list1 = list1.next
                dummy = dummy.next
            elif list2.val < list1.val:

                dummy.next = list2
                list2 = list2.next

                dummy = dummy.next
            elif list1.val == list2.val:

                dummy.next = list1
                list1 = list1.next
                # list2 = list2.next
                dummy = dummy.next
        # if list1 is not None:
        #     dummy.next = list1
        # else:
        #     dummy.next =list2
        # return head.next         
        while list1 is not None:
            dummy.next = list1
            list1 = list1.next
            dummy = dummy.next
        while list2 is not None:
            dummy.next = list2
            list2 = list2.next
            dummy = dummy.next

        return head.next

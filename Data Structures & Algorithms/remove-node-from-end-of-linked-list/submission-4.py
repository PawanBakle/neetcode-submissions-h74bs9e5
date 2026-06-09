
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head
        N = 0 # to calculate the len of the LL
        # if N == 1 and n == 1:
        #     head = None
        #     return head
        while cur is not None:
            N+=1
            cur = cur.next       
        target_index  = N - n
        if target_index  == 0:
            return head.next
        current_index = 0
        current_node = head
        previous_node = None
        while current_node is not None:
            if current_index == target_index:
                previous_node.next = current_node.next
                break
            # else:
            current_index +=1
            previous_node = current_node
            current_node = current_node.next

        return head
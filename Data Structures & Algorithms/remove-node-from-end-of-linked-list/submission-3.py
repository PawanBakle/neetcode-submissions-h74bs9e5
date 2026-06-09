
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # cur = head
        # arr = []
        # while cur is not None:
        #     arr.append(cur.val)
        #     cur = cur.next
        # length = len(arr)
        # for i in range(len(arr) - 1, -1, -1):
        #     if (length - i) == n: 
        #         arr.pop(i)
        #         break
        # if len(arr) == 0:
        #     return None
        # head = ListNode(arr[0])
        # cur = head

        # for i in range(1,len(arr)):
        #     new_node = ListNode(arr[i])
        #     cur.next = new_node
        #     # new_node = cur  # This does nothing to advance 'cur'. 'cur' stays at the head forever
        #     cur = new_node
        #     # arr[i] = ListNode()

        # return head

        cur = head
        
        N = 0
        # if N == 1 and n == 1:
        #     head = None
        #     return head
        while cur is not None:
            N+=1
            cur = cur.next

       
        cnt = N - n
        if cnt == 0:
            return head.next
        prev = None
        pointer = head
        c_out = 0
        while pointer is not None:
            if c_out == cnt:
                prev.next = pointer.next
                break
            # else:
            c_out +=1
            prev = pointer
            pointer = pointer.next

        return head
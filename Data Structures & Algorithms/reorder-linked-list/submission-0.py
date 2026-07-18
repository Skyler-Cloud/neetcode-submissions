# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = head
        curr = head
        length = 0
        while curr:
            length +=1
            if length %2==1:
                mid = mid.next
            curr = curr.next
        # reverse last half
        curr = None
        while mid:
            temp = mid.next
            mid.next = curr
            mid, curr = temp, mid
        # interleave now
        while head is not None:
            head.next, head, curr = curr, curr, head.next


            
                

        
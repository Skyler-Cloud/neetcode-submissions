# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2 or list1.val<list2.val:
            head=list1
            other = list2
        else:
            head = list2
            other = list1
        curr = head
        while other:
            if not curr.next or curr.next.val > other.val:
                curr.next,other=other,curr.next
            else:
                curr=curr.next
        return head
            

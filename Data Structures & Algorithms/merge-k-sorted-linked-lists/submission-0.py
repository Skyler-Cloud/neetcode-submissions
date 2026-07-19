# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        head = lists[0]
        for l in lists[1:]:
            if l is None:
                continue
            if head is None or l.val < head.val:
                head,l = l,head
            curr = head
            while l:
                if curr.next is None or l.val < curr.next.val:
                    curr.next,l=l,curr.next
                curr = curr.next
        return head

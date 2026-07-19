# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.merge(lists)
    def merge(self, lists):
        if len(lists)==1:
            return lists[0]
        if len(lists)==0:
            return None
        l1 = self.merge(lists[:len(lists)//2])
        l2 = self.merge(lists[len(lists)//2:])
        if l1 is None or l2.val < l1.val:
            l1,l2=l2,l1
        head = l1
        while l2:
            if l1.next is None or l2.val < l1.next.val:
                l1.next,l2=l2,l1.next
            l1 = l1.next
        return head
            

        

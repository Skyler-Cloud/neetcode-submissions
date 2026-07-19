# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Recursive
        def kth(node,rank): # (True,val) or (False,total num in graph)
            tot = 1
            if node.left:
                isans, val = kth(node.left,rank)
                if isans:
                    return True,val
                tot += val
            if tot == rank:
                return True,node.val
            if node.right:
                isans,val = kth(node.right,rank-tot)
                if isans:
                    return True,val
                tot += val
            return False,tot
        return kth(root,k)[1]
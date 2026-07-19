# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Same thing but Iterative
        dq = deque([root])
        rank = 0
        while dq:
            node = dq.pop()
            if isinstance(node,int):
                rank += 1
                if rank == k:
                    return node
            else:
                dq.extend([thing for thing in [node.right, node.val, node.left] if thing is not None])
        
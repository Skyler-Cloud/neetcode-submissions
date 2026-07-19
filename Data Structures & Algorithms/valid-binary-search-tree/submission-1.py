# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # iterative naive solution (queue of tuples)
        if root is None:
            return True
        dq = deque([(root,None,None)])
        while dq:
            node,floor,ceil = dq.popleft()
            if (floor is not None and node.val<=floor) or (ceil is not None and node.val>=ceil):
                return False
            if node.left:
                dq.append((node.left,floor,node.val))
            if node.right:
                dq.append((node.right,node.val,ceil))
        return True
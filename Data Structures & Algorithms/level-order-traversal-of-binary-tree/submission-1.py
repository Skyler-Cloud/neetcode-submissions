# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        dq=deque([root])
        nodes = []
        while dq:
            n=len(dq)
            curr_lev = []
            for _ in range(n):
                node = dq.popleft()
                curr_lev.append(node.val)
                dq.extend([thing for thing in [node.left,node.right] if thing])
            nodes.append(curr_lev)
        return nodes
        
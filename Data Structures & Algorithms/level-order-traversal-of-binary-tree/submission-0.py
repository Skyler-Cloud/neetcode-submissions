# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq=deque([(root,0)])
        nodes = []
        while dq:
            node,lev = dq.popleft()
            if node is None:
                continue
            if lev==len(nodes):
                nodes.append([node.val])
            else:
                nodes[lev].append(node.val)
            dq.extend([(node.left,lev+1),(node.right,lev+1)])
        return nodes
        
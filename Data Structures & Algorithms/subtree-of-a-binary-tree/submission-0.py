# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        return self.equal(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
    def equal(self, root,subRoot):
        dq = deque([(root,subRoot)])
        while dq:
            (a,b)=dq.popleft()
            if a is None or b is None:
                if a != b:
                    return False
            elif a.val != b.val:
                return False
            else:
                dq.extend([(a.left,b.left),(a.right,b.right)])
        return True

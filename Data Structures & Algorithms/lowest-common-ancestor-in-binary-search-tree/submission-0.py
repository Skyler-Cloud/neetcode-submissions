# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.found(root,p,q)[-1]
    def found(self,root,p,q):
        if root is None:
            return (False,False,None)
        lp,lq,lnode = self.found(root.left,p,q)
        if lp and lq:
            return (True,True,lnode)
        rp,rq,rnode = self.found(root.right,p,q)
        if rq and rp:
            return (True,True,rnode)
        isP = root.val==p.val
        isQ = root.val==q.val
        
        if (lp or rp or isP) and (lq or rq or isQ):
            return (True,True, root)
        return (lp or rp or isP), (lq or rq or isQ), None
    
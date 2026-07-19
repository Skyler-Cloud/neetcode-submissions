# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        # recursive solution
        def isValidBST(node,floor,ceil): # floor and ceiling of the subtree
            if (floor is not None and node.val<=floor) or (ceil is not None and node.val>=ceil):
                return False
            if node.left:
                curr_val = isValidBST(node.left,floor,node.val)
                if not curr_val:
                    return False
            if node.right:
                return isValidBST(node.right,node.val,ceil)
            return True
        return isValidBST(root,None,None)
            
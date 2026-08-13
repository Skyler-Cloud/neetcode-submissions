# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # at every node, max 2 are between [max left+curr, maxright+curr, curr val]
        # needs DFS
        #idea: edit the val of nodes to be a tuple of max 2 paths starting from that node.
        maxsum = root.val
        tovisit = []
        curr = root
        tofill = []
        while tovisit or curr:
            while curr:
                tofill.append(curr)
                if curr.right:
                    tovisit.append(curr.right)
                curr=curr.left
            if tovisit:
                curr = tovisit.pop()
        while tofill:
            curr = tofill.pop()
            left = max(0,curr.left.val if curr.left else 0)
            right = max(0, curr.right.val if curr.right else 0)

            maxsum = max(maxsum, curr.val + left + right)
            curr.val += max(left,right)
        return maxsum
            

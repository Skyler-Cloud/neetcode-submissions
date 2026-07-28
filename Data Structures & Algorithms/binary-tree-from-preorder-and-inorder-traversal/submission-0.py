# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. while preorder node != inorder, put node as a left child and go down
        # 2. when it does equal, go up the parents until parent no longer equals inorder. 
            # 3. stay at last node to match the inorder traversal.
            # 4. set the right child to the preorder node and repeat from 1. 
        # stop condition: end of preorder list?
        head = TreeNode(preorder[0])
        curr = head
        stack = []
        prei,ini = 0,0
        while prei < len(preorder):
            if preorder[prei] != inorder[ini]:
                prei += 1
                while True:
                    curr.left = TreeNode(preorder[prei])
                    stack.append(curr)
                    curr = curr.left
                    if preorder[prei] == inorder[ini]:
                        break
                    prei += 1
                    
            prei +=1
            ini += 1
            while stack:
                if stack[-1].val != inorder[ini]:
                    break
                curr = stack.pop()
                ini += 1
            if prei<len(preorder):
                curr.right = TreeNode(preorder[prei])
                curr = curr.right
        return head
            
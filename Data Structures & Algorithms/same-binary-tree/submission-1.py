# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative Solution
        queue = deque([(p,q)])
        while len(queue)>0:
            (a,b) = queue.popleft()
            print(a.val if a is not None else a)
            print(b.val if b is not None else b)
            print()
            if a is None or b is None:
                if a != b:
                    return False
            elif a.val != b.val:
                return False
            else:
                queue.extend([(a.left,b.left),(a.right,b.right)])
        return True
            
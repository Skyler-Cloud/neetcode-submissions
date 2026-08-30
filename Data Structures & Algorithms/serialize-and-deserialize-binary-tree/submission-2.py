# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '#'
        curr = root
        nodes = []
        stack =[]
        while curr or stack:
            while curr:
                nodes.append(f'{curr.val}')
                stack.append(curr.right)
                curr = curr.left
            nodes.append('#')
            curr= stack.pop()
        return ','.join(nodes)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '#':
            return
        nodes = data.split(',')
        root = TreeNode()
        parents = [] # parents missing right child processing
        curr, right = root, False
        for val in nodes:
            if val == '#':
                # handle go to next unmarked right child
                curr= parents.pop()
                right = True
                continue

            if right:
                curr.right = TreeNode(int(val))
                curr=curr.right
            else:
                curr.left = TreeNode(int(val))
                curr=curr.left
            parents.append(curr)
            right = False
        return root.left

            

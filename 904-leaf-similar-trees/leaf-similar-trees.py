# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_1 = []
        leaf_2 = []
        self.traverseTree(root1, leaf_1)
        self.traverseTree(root2, leaf_2)
        return leaf_1 == leaf_2
        
    def traverseTree(self, root: Optional[TreeNode], leaf: list[int]):
        if not root:
            return
        if not root.left and not root.right:
            leaf.append(root.val)
        self.traverseTree(root.left, leaf)
        self.traverseTree(root.right, leaf)

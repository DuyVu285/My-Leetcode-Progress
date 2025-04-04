# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxDepth = self.maxDepth(root)
        currentDepth = 0
        return self.treeTraversal(root, maxDepth, currentDepth)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
    def treeTraversal(self, node: Optional[TreeNode], maxDepth: int, depth: int) -> Optional[TreeNode]:
        if depth == maxDepth - 1:
            return node
        left = right = None
        if node:
            if node.left:
                left = self.treeTraversal(node.left, maxDepth, depth+1)
            if node.right:
                right = self.treeTraversal(node.right, maxDepth, depth+1)
        if left and right:
            return node
        return left if left else right
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traversal(root)
        
    def traversal(self, node):
        if not node:
            return 0
        left_count = self.traversal(node.left)
        right_count = self.traversal(node.right)
        return 1 + left_count + right_count
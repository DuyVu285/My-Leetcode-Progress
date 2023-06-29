# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preorder = []
        if root is not None:
            self.traversal(root, preorder)
            
        return preorder
    def traversal(self, node, preorder):
        if node is None:
            return 
        
        if node is not None:
            preorder.append(node.val)
            self.traversal(node.left, preorder)
            self.traversal(node.right, preorder)
            
        return preorder
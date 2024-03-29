# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self,node1, node2):
        if node1 is None and node2 is None:
            return True
        
        if node1 is None or node2 is None:
            return False
        
        return (
        node1.val == node2.val and
        self.isMirror(node1.left, node2.right) and
        self.isMirror(node1.right, node2.left)
        )
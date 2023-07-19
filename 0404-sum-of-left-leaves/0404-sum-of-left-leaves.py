# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return self.recursive(root)

    def recursive(self, node):
        result = 0
        
        if node.left is not None:
            if not node.left.left and not node.left.right:    
                result += node.left.val
            else:
                result += self.recursive(node.left)
            
        if node.right is not None:
            result += self.recursive(node.right)
            
        return result
            
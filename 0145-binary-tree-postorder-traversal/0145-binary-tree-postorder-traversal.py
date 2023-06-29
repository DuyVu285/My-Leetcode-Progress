# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        postorder = []
        if root is not None:
            self.traversal(root, postorder)
            
        return postorder
    
    def traversal(self, node, postorder):
        if node is None:
            return
        
        if node is not None:
            self.traversal(node.left, postorder)
            self.traversal(node.right, postorder)
            postorder.append(node.val)
            
        return postorder
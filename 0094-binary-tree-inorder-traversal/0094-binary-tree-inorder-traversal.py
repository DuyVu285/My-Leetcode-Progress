# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.inorder_helper(root, output)
        return output
    
    def inorder_helper(self, node, output):
        if node:
            self.inorder_helper(node.left,output)
            output.append(node.val)
            self.inorder_helper(node.right,output)
        
            
            
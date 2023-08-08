# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def inorder_traversal(node):
            if not node:
                return False

            if k - node.val in visited:
                return True

            visited.add(node.val)

            return inorder_traversal(node.left) or inorder_traversal(node.right)
    
        visited = set()
        return inorder_traversal(root)
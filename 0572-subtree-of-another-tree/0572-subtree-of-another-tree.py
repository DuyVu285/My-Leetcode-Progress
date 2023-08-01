# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if self.isMatch(root, subRoot): return True
        if not root: return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isMatch(self, s, t):
        if not (s and t):
            return s is t
        return (s.val == t.val and 
            self.isMatch(s.left, t.left) and 
            self.isMatch(s.right, t.right))
        
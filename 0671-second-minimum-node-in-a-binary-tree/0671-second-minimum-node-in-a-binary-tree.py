# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            a.append(root.val)
            dfs(root.right)

        dfs(root)

        return (sorted(set(a)))[1] if len(set(a)) >= 2 else -1
        
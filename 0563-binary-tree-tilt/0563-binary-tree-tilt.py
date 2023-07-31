# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_tilt = dfs(node.left)
            right_sum, right_tilt = dfs(node.right)

            total_sum = node.val + left_sum + right_sum
            current_tilt = abs(left_sum - right_sum) + left_tilt + right_tilt

            return total_sum, current_tilt

        _, result = dfs(root)
        return result
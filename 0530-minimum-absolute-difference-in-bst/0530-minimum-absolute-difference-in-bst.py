# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def in_order_traversal(node, prev, min_diff):
            if not node:
                return min_diff, prev

            min_diff, prev = in_order_traversal(node.left, prev, min_diff)

            if prev is not None:
                min_diff = min(min_diff, abs(node.val - prev))

            prev = node.val

            min_diff, prev = in_order_traversal(node.right, prev, min_diff)

            return min_diff, prev

        min_diff, _ = in_order_traversal(root, None, float('inf'))
        return min_diff






        
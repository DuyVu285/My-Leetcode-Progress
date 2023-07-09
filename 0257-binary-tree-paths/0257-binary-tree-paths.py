# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        def dfs(node, path, result):
            if not node.left and not node.right:
                path.append(str(node.val))
                result.append("->".join(path))
                path.pop()
                return

            path.append(str(node.val))
            if node.left:
                dfs(node.left, path, result)
            if node.right:
                dfs(node.right, path, result)
            path.pop()

        result = []
        dfs(root, [], result)
        return result
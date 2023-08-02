"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        self.traversal(root, result)
        return result
    def traversal(self, node, result):
        for child in node.children:
            self.traversal(child, result)
        result.append(node.val)
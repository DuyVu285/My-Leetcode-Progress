"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        
        return self.traverse(root, 1)
    
    def traverse(self, node, depth):
        max_depth = depth
        if node.children:
            for child in node.children:
                max_depth = max(max_depth, self.traverse(child, depth+1))
        return max_depth
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node_counts = {}
        self.traverse(root, node_counts)
        
        max_count = max(node_counts.values()) if node_counts else 0
        
        # Find the mode(s) based on the max count
        modes = [key for key, count in node_counts.items() if count == max_count]
        
        return modes
    
    def traverse(self, node, count_dict):
        if not node:
            return

        count_dict[node.val] = count_dict.get(node.val, 0) + 1

        self.traverse(node.left, count_dict)
        self.traverse(node.right, count_dict)

            
        
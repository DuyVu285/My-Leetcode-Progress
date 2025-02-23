# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        
        # Create a mapping from value to index in postorder for fast lookup
        postorder_index = {val: i for i, val in enumerate(postorder)}
        
        # Preorder index tracker
        self.preIndex = 0
        
        def construct(left: int, right: int) -> Optional[TreeNode]:
            if left > right or self.preIndex >= len(preorder):
                return None
            
            # Create root node
            root_val = preorder[self.preIndex]
            root = TreeNode(root_val)
            self.preIndex += 1
            
            # If there's only one node left, return it
            if left == right or self.preIndex >= len(preorder):
                return root
            
            # Get left child index in postorder
            left_child_val = preorder[self.preIndex]
            left_child_index = postorder_index[left_child_val]
            
            # Recursively construct left and right subtrees
            root.left = construct(left, left_child_index)
            root.right = construct(left_child_index + 1, right - 1)  # Exclude root (postorder[right])
            
            return root
        
        return construct(0, len(postorder) - 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self.recoverTree(root, 0)

    def recoverTree(self, node: Optional[TreeNode], value: int):
        if not node:
            return
        node.val = value
        self.values.add(value)
        self.recoverTree(node.left, 2*value+1)
        self.recoverTree(node.right, 2*value+2)  

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
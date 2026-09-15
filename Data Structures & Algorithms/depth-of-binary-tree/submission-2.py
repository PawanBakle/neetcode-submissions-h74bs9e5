# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # first check for last Node  /
        if root is None:
            return 0
        # collect the left / right Subtree
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # once calls are collected 
        # post-order computation to get the len
        return max(left,right) + 1
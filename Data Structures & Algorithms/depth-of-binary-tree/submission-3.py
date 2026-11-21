# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        # left = root.left
        # right = root.right
        left_call = self.maxDepth(root.left) # will return a value
        right_call = self.maxDepth(root.right) # will return a value
        return max(left_call,right_call) + 1
        
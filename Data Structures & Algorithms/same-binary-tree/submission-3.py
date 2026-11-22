class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        if p.val == q.val:
                left = self.isSameTree(p.left, q.left)
                right = self.isSameTree(p.right,q.right)
                if left == True and right == True:
                    return True
                else:
                    return False
        else:
            return False

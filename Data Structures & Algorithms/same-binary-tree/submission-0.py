# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        # Both nodes are empty: same
        if not p and not q:
            return True

        # Only one node is empty: different
        if not p or not q:
            return False

        # Values are different
        if p.val != q.val:
            return False

        # Both left sides AND both right sides must match
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
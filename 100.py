# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # if both are empty (true)
            return True
        if not p or not q or p.val != q.val: # if one is empty and the other is not
            return False
        return(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))



print(Solution().isSameTree(p = Optional[1,2,1], q = Optional[1,2,1]))

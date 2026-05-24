from typing import Optional
from tree_node import TreeNode

class Solution:

    def calTilt(self,root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #Find sum of left sub tree and right sub-tree
        lsum = self.calTilt(root.left)
        rsum = self.calTilt(root.right)
        #tilt is absolute difference between left sub-tree sum and right sub-tree sum
        tilt = abs( lsum - rsum)
        self.total_tilt += tilt
        total = root.val + lsum + rsum
        root.val = tilt
        return total

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0
        self.calTilt(root)
        return self.total_tilt
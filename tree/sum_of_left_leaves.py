from typing import Optional
from tree_node import TreeNode
class Solution:

    def getSum(self, root, dir):
        if root is None:
            return 0
        # Check if its a leaf node
        if root.left == None and root.right == None:
            if dir == 'l':  # if left leaf
                return root.val
            else:
                return 0
        # Check recursively the left and right child of the root
        return self.getSum(root.left, 'l') + self.getSum(root.right, 'r')

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.getSum(root, 'c')

    
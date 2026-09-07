from typing import Optional
from tree_node import TreeNode

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #Initialise total sum
        total = 0
        if root.val % 2 == 0:
            #Check left sub tree
            if root.left:
                if root.left.left:
                    total += root.left.left.val
                if root.left.right:
                    total += root.left.right.val
            #Check right sub tree
            if root.right:
                if root.right.left:
                    total += root.right.left.val
                if root.right.right:
                    total += root.right.right.val
        #Recursively traverse and explore the left and right subtrees.
        return total + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)

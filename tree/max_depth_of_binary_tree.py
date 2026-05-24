from tree_node import TreeNode
from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #Leaf node so return 1
        if root.left == None and root.right == None:
            return 1
        #Current node's depth is 1 + max depth from its children
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
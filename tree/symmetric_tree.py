from typing import Optional
from tree_node import TreeNode

class Solution:

    def check(self,p:Optional[TreeNode],q:Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif ((p != None and q == None) or (p == None and q != None)
                 or (p.val != q.val)):
                return False
        #Check left child of a node with right child of the mirror node
        #and vice versa
        return self.check(p.left,q.right) and self.check(p.right,q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.check(root.left,root.right)
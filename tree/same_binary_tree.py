from typing import Optional
from tree_node import TreeNode

class Solution:
    def isSame(self,p,q):
        if p == None and q == None:
            return True
        if ((p == None and q != None) or (p != None and q == None) or (p.val != q.val)):
            return False
        return self.isSame(p.left,q.left) and self.isSame(p.right,q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSame(p,q)
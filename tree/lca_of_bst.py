from tree_node import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr, ans = root, None

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                ans = curr #(p.val <= curr.val && curr.val >= q.val) || (q.val <= curr.val && curr.val >= p.val)
                break

        return curr
from collections import deque
from tree_node import TreeNode

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        ans = []
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            total = 0
            for _ in range(size):
                curr = q.popleft()
                total += curr.val
                # Check for left and right child
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            # Take average
            ans.append(total / size)

        return ans
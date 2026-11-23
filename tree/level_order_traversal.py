from collections import deque

class Solution:
    def levelOrder(self, root):
        # code here
        if not root:
            return []
        q = deque()
        ans = []
        # Add root to queue
        q.append(root)

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                ans.append(curr.data)
                # Push left child
                if curr.left:
                    q.append(curr.left)
                # Push right child
                if curr.right:
                    q.append(curr.right)

        return ans
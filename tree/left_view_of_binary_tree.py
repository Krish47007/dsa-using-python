from collections import deque

class Solution:
    def leftView(self, root):
        # code here
        ans = []
        if not root:
            return ans

        q = deque()
        q.append(root)

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if i == 0:
                    ans.append(curr.data)
                # Push in queue if curr has children
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return ans
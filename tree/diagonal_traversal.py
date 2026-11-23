from collections import deque

class Solution:

    def diagonal(self, root):
        # code here
        ans = []
        q = deque()
        q.append(root)

        while q:
            # Pop from queue
            curr = q.popleft()
            # Traverse until we reach null
            while curr:
                # Add to answer
                ans.append(curr.data)
                # Push left child to queue
                if curr.left:
                    q.append(curr.left)
                # Traverse right
                curr = curr.right

        return ans
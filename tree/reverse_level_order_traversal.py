from collections import deque

class Solution:
    def reverseLevelOrder(self, root):
        ans = []
        if not root:
            return ans

        q = deque()
        # Add root
        q.append(root)

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                ans.append(curr.data)
                # Put right child first
                if curr.right:
                    q.append(curr.right)
                # Now put left child
                if curr.left:
                    q.append(curr.left)

        # Reverse the list
        ans.reverse()

        return ans
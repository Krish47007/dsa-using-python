from collections import deque as dq

from collections import deque

class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []

        dq = deque()
        dq.append((root, 0))
        view_map = {}

        while len(dq):
            node, x = dq.popleft()
            view_map[x] = node.data
            if node.left:
                dq.append((node.left, x - 1))

            if node.right:
                dq.append((node.right, x + 1))

        ans = []
        for key in sorted(view_map):
            ans.append(view_map[key])

        return ans
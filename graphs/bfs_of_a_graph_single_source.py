from collections import deque
#This problem specifies the BFS to be done starting from a single source that is 0.
class Solution:
    def bfs(self, adj):
        n = len(adj)
        # Create visited array
        vis = [0] * n
        q = deque()
        # Start from the first node and mark it as visited
        q.append(0)
        vis[0] = 1
        ans = []

        while q:
            curr = q.popleft()
            ans.append(curr)
            # Check the connections
            for conn in adj[curr]:
                # If unvisited then push to queue
                if vis[conn] == 0:
                    vis[conn] = 1
                    q.append(conn)

        return ans
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Declare Adjacency list
        adj = [[] for _ in range(n)]
        vis = [0] * n
        # Build adjacency list
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        ans = 0

        # Perform DFS traversal
        def dfs(curr):
            vis[curr] = 1
            self.nodes += 1
            self.totalEdges += len(adj[curr])

            for conn in adj[curr]:
                if vis[conn] == 0:
                    dfs(conn)

        for i in range(n):
            # Start of the component
            if vis[i] == 0:
                self.nodes, self.totalEdges = 0, 0
                dfs(i)
                # For complete components the following holds
                if (self.nodes * (self.nodes - 1)) == self.totalEdges:
                    ans += 1

        return ans



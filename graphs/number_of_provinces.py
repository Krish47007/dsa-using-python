from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [0] * n
        count = 0

        def dfs(curr):
            vis[curr] = 1
            for conn in range(len(isConnected[curr])):
                #If the node is unvisited and connected to curr
                if vis[conn] == 0 and isConnected[curr][conn] == 1:
                    dfs(conn)

        for i in range(n):
            if vis[i] == 0:
                #Start of the component
                count += 1
                dfs(i)

        return count
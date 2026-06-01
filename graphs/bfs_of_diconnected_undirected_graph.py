from collections import deque
class Solution:
    def peform_bfs(self,adj):
        n = len(adj)
        #Create a visited array
        vis = [False] * n
        ans = []

        def bfs(start):
            #Start is the starting point of a component
            q = deque()
            q.append(start)
            vis[start] = True
            while q:
                curr = q.popleft()
                ans.append(curr)
                #Traverse the adjacency list
                for conn in adj[curr]:
                    if not vis[conn]:
                        vis[conn] = True
                        q.append(conn)

        #Traverse the visited array
        for i in range(n):
            #If unvisited
            if not vis[i]:
                bfs(i)

        return ans


obj = Solution()
'''
0 --- 1

|     |

2     3

4 --- 5 --- 6

7 --- 8
'''
ans = obj.peform_bfs([[1, 2],[0, 3],[0],[1],[5],[4, 6],[5],[8],[7]])
print(ans)
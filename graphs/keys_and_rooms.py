from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        self.count = 0
        vis = [0] * n

        def dfs(curr):
            self.count += 1
            vis[curr] = 1
            #Iterate over the rooms that curr unlocks
            for conn in rooms[curr]:
                if vis[conn] == 0:
                    dfs(conn)
        #Starting from 0th room
        dfs(0)
        #If all rooms can be visited then true
        return self.count == n

    #The following approach solves the same problem using BFS
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        count = 0
        vis = [False] * n

        def bfs(start):
            q = deque()
            q.append(start)
            vis[start] = True
            while q:
                curr = q.popleft()
                self.count += 1
                for conn in rooms[curr]:
                    if not vis[conn]:
                        # Mark as visited
                        vis[conn] = True
                        q.append(conn)
        #Room 0 is unlocked
        bfs(0)
        #If all rooms are visited
        return self.count == n
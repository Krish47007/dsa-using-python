from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a,b = edges[0][0], edges[0][1]

        #Since its a star graph so either a will be same as
        #one of the nodes next to it or b
        if a == edges[1][0] or a == edges[1][1]:
            return a
        else:
            return b
from node import Node

class Solution:

    def getNode(self, head: 'Node', k: int) -> int:

        ans = -1
        if not head:
            return ans

        temp, pos = head, 1

        while temp:
            if pos == k:
                ans = temp.data
                break
            # Move temp and increment pos
            temp = temp.next
            pos += 1

        return ans
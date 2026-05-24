from list_node import ListNode
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next # Move fast by two nodes
            slow = slow.next      # Move slow by one
            # If fast and slow meet, then it's a cycle
            if fast == slow:
                return True

        return False
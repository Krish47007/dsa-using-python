
from typing import Optional
from list_node import ListNode

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        fast, slow = head, head
        # Start looping
        while fast and fast.next:
            # Move slow by 1 and fast by 2
            slow = slow.next
            fast = fast.next.next

        return slow

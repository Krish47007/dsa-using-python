from typing import Optional
from list_node import ListNode

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If empty list or only one node
        if not head or not head.next:
            return head

        curr = head
        while curr:
            nextNode = curr.next
            # Check if next node is same as curr
            while nextNode and nextNode.val == curr.val:
                nextNode = nextNode.next
            # Point curr's next to nextNode and change curr
            curr.next = nextNode
            curr = nextNode

        return head

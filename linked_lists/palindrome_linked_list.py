from typing import Optional
from list_node import ListNode

class Solution:

    def reverse(self, head):
        if not head:
            return None
        prev, curr = None, head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev

    def getMid(self, head):
        if not head:
            return None
        slow = fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        mid = self.getMid(head)
        # break from mid
        nextNode = mid.next
        mid.next = None
        # Reverese the second half
        newHead = self.reverse(nextNode)
        curr1, curr2 = head, newHead

        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next

        return True

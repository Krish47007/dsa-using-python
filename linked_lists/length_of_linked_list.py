''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:

    def getCount(self, head):
        count = 0
        if not head:
            return count
        # temp nodes point to head initially
        temp = head
        while temp:
            count += 1
            temp = temp.next

        return count
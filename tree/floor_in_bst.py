class Solution:
    def findMaxFork(self, root, k):
        # code here
        curr, ans = root, -1

        while curr:
            if curr.data == k:
                ans = curr.data
                break
            elif curr.data < k:
                # Check if the curr's val > previously stored val
                ans = max(ans, curr.data)
                curr = curr.right
            else:
                # Simply go left
                curr = curr.left

        return ans
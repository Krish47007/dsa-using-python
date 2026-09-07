class Solution:
    def findCeil(self, root, x):
        # code here
        curr, ans = root, float('inf')
        while curr:
            if curr.data == x:
                ans = curr.data
                break
            elif curr.data > x:
                ans = min(ans, curr.data)
                curr = curr.left
            else:
                curr = curr.right

        return -1 if ans == float('inf') else ans
#1st solution
"""
class Solution:
    def maxSubarraySum(self, arr, k):
        n,total = len(arr),0

        #Cal the sum of first window
        for i in range(k):
            total += arr[i]

        beg,end,maxSum = 0, k, total

        while end < n:
            total -= arr[beg]
            total += arr[end]
            maxSum = max(maxSum,total)
            beg += 1
            end += 1

        return maxSum
"""


class Solution:
    def maxSubarraySum(self, arr, k):
        l, r, n = 0, 0, len(arr)
        maxSum = total = 0

        while r < n:
            total += arr[r]
            # Check if current window size is > k
            if (r - l + 1) > k:
                total -= arr[l]
                l += 1
            # Take the max sum of current window and previously stored sum
            maxSum = max(maxSum, total)
            r += 1

        return maxSum

obj = Solution()
print(obj.maxSubarraySum([1, 4, 2, 10, 23, 3, 1, 0, 20],4))
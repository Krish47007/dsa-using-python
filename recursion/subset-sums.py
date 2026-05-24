class Solution:
    def subsetSums(self, arr):
        n = len(arr)
        ans = []

        def calSum(i, curr_sum):
            if i == n:
                ans.append(curr_sum)
                return

            # Take
            calSum(i + 1, curr_sum + arr[i])
            # Not take
            calSum(i + 1, curr_sum)

        calSum(0, 0)

        return ans

obj = Solution()
res = obj.subsetSums([1,2,3])
res.sort()
print(res)
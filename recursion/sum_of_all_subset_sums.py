class Solution:

    def get_all_subset_sums(self,nums):
        totalSum = 0
        n = len(nums)

        def calSum(i, curr_sum):
            nonlocal totalSum
            if i == n:
                totalSum += curr_sum
                return
            calSum(i + 1, curr_sum + nums[i])
            calSum(i + 1, curr_sum)

        #calculate the sums
        calSum(0,0)

        return totalSum

obj = Solution()
print(obj.get_all_subset_sums([1,2,3]))

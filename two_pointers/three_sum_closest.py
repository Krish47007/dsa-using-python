from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')
        ans = 0

        for i in range(n - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                #Need to take absolute value as dist
                dist = abs(target - total)

                if dist < closest:
                    closest = dist
                    ans = total

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return target  # exact match so return

        return ans
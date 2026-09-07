from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        minDist = float('inf')
        closestSum = 0

        for i in range(n-2):
            j,k = i+1,n-1

            while( j < k):
                total = nums[i] + nums[j] + nums[k]
                #Take the abs. value of diff.
                dist = abs(target - total)
                if dist < minDist:
                    minDist = dist
                    closestSum = total
                elif total > target:
                    k -= 1
                else:
                    j += 1

        return closestSum
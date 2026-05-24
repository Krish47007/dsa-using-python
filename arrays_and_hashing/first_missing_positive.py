
from typing import List

class Solution:
    '''
         +ve number starts from 1 and in an array of size n max upto n we can store.
        If our array size is n and even if we store all the numbers from 1 to n
        then in worst case missing +ve is n+1.
        Ex -  arr = [1,2,3] , n = 3 so first missing is n + 1 = 4
    '''

    def firstMissingPositive(self, nums: List[int]) -> int:
        mySet = set()
        n = len(nums);
        # Add the number in Set
        for i in range(n):
            mySet.add(nums[i])

        # Now check from num 1 to n
        for i in range(1, n + 1):
            # If i is not present in set then its first missing +ve
            if i not in mySet:
                return i

        # If all the nums from 1 to n are there in nums
        return n + 1

    def firstMissingPositive_1(self, nums: List[int]) -> int:

        n = len(nums)
        # Mark all -ve numbers as 0
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        # Scan through the array and mark the numbers that exist in array
        # to its -ve counterpart
        for i in range(n):
            temp = abs(nums[i])
            if 1 <= temp <= n:
                if nums[temp - 1] > 0:
                    nums[temp - 1] *= -1  # If its +ve then make it -ve
                elif nums[temp - 1] == 0:  # if its 0 then replace with -(n+1)
                    nums[temp - 1] = -1 * (n + 1)
                # Already -ve numbers we dont touch

        # Scan from 1 to n and see if it exists
        for i in range(1, n + 1):
            if nums[i - 1] >= 0:
                return i  # first missing +ve

        # all the numbers from 1 to n exists in array so next missing is n+1
        return n + 1

obj = Solution()
print(obj.firstMissingPositive_1([-12,23,1,3,4,2,8]))

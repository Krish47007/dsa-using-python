from typing import List


class Solution:
    def increasingNumbers(self, n: int) -> List[int]:
        # code here
        ans = []
        # If its single digit numbers
        if n == 1:
            for i in range(10):
                ans.append(i)
            return ans

        def rec(k, prev, num):
            if k == 0:
                ans.append(num)
                return

            for digit in range(prev + 1, 10):
                rec(k - 1, digit, num * 10 + digit)

        rec(n, 0, 0)

        return ans


obj = Solution()
print(obj.increasingNumbers(2))
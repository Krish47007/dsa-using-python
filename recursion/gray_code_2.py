from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]

        half = self.grayCode(n - 1)

        ans = []

        # Copy 1st half as it is
        for i in range(len(half)):
            ans.append(half[i])

        for i in range(len(half) - 1, -1, -1):
            ans.append(half[i] + int(pow(2, n - 1)))

        return ans

obj = Solution()
print(obj.grayCode(2))
print(obj.grayCode(3))
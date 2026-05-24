from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_map = {}
        l, r = 0, 0
        ans, n = 0, len(fruits)

        while r < n:
            fruit_map[fruits[r]] = fruit_map.get(fruits[r], 0) + 1
            # Check if we have more than 2 types of fruits in the basket
            while l <= r and len(fruit_map) > 2:
                count = fruit_map[fruits[l]] - 1
                if count != 0:
                    fruit_map[fruits[l]] = count
                else:
                    fruit_map.pop(fruits[l])

                l += 1

            ans = max(ans, r - l + 1)
            r += 1

        return ans
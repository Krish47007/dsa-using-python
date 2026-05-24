from typing import List
import heapq as h

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for i in range(len(nums)):
            h.heappush(min_heap, nums[i])
            if len(min_heap) > k:
                h.heappop(min_heap)

        return min_heap[0]

obj = Solution()
print(obj.findKthLargest([2,3,2,4,5],2))
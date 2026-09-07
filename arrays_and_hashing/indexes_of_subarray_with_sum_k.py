class Solution:
    def subarraySum(self, arr, k):
        # code here
        n = len(arr)
        _map = {}
        total = 0

        for i in range(n):
            total += arr[i]
            # If sum is k or sum repeats then we have a sub array sum k
            if total == k:
                return [1, i + 1]
            elif (total - k) in _map:
                return [_map[total - k] + 2, i + 1]

            _map[total] = i

        return [-1]
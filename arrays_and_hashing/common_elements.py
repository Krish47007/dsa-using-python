class Solution:
    def commonElements(self, a, b):
        # code here
        _map = {}
        for x in a:
            _map[x] = _map.get(x, 0) + 1

        ans = []

        for x in b:
            if x in _map:
                ans.append(x)
                count = _map[x] - 1
                if count == 0:
                    _map.pop(x)
                else:
                    _map[x] = count

        ans.sort()
        return ans

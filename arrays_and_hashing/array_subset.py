class Solution:
    # Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        n, m = len(a), len(b)
        _map = {}

        for x in a:
            _map[x] = _map.get(x, 0) + 1

        for y in b:
            if y not in _map:
                return False
            else:
                _map[y] -= 1
                if _map[y] == 0:
                    _map.pop(y)

        return True




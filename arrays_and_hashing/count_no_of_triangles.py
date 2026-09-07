class Solution:
    def countTriangles(self, arr):
        # code here
        arr.sort()
        count = 0
        n = len(arr)

        for c in range(n - 1, 1, -1):
            b = c - 1
            a = 0
            while a < b:
                if arr[a] + arr[b] > arr[c]:
                    count += (b - a)
                    b -= 1
                else:
                    a += 1

        return count
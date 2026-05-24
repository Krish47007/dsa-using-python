
class Solution:

    def permutation(self, str):
        # code here
        ans = []
        n = len(str)
        if n == 0:
            return ans
        def rec(i, s):
            if i == n - 1:
                ans.append(s + str[n - 1])
                return

            # Add char and space
            rec(i + 1, s + str[i] + " ")
            # No Space
            rec(i + 1, s + str[i])

        rec(0, "")
        return ans

ob = Solution()
print(ob.permutation("abc"))
print(ob.permutation("a"))
print(ob.permutation(""))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        # If the lengths are unequal
        if n != m:
            return False
        # Create a freq array
        freq = [0] * 26

        for i in range(n):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        for i in range(26):
            if freq[i] != 0:
                return False

        return True

obj = Solution()
print(obj.isAnagram("race","care"))
print(obj.isAnagram("race","rcare"))
print(obj.isAnagram("race","racc"))
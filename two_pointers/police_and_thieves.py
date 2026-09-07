class Solution:
    def catchThieves(self, nums, k):
        # code here
        n = len(nums)
        police, thief = 0, 0

        # Make police point to first police
        while (police < n and nums[police] == 'T'):
            police += 1
        # Make thief point to first thief
        while (thief < n and nums[thief] == 'P'):
            thief += 1

        count = 0

        while (police < n and thief < n):
            if abs(police - thief) <= k:
                count += 1
                # move police and thief
                police += 1
                thief += 1
                # Make sure police and thief points correctly
                while (police < n and nums[police] == 'T'):
                    police += 1
                while (thief < n and nums[thief] == 'P'):
                    thief += 1
            else:
                # If police is away look for next thief
                if police > thief:
                    thief += 1
                    while (thief < n and nums[thief] == 'P'):
                        thief += 1
                else:  # thief is away he can be caught by next police
                    police += 1
                    # Move police if needed
                    while (police < n and nums[police] == 'T'):
                        police += 1

        return count


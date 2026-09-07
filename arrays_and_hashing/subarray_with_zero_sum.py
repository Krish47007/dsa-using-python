class Solution:

    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr):
        ##Your code here
        # Return true or false
        n = len(arr)
        hash_set = set()
        total = 0

        for i in range(n):
            total += arr[i]
            # If sum is 0 or sum repeats then we have a sub array sum 0
            if total == 0 or total in hash_set:
                return True
            hash_set.add(total)

        return False
class Solution:
    def getSecondLargest(self, arr):

        largest, second_largest = -1, -1

        for x in arr:
            if x > largest:
                second_largest = largest
                largest = x
            elif x > second_largest and x != largest:
                second_largest = x

        return second_largest


obj = Solution()
print(obj.getSecondLargest([12, 35, 1, 10, 34, 1]))
print(obj.getSecondLargest([10, 5, 10]))
print(obj.getSecondLargest([10, 10, 10]))
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        largest,second_largest,third_largest = float('-inf'),float('-inf'),float('-inf')

        for n in nums:
            if n > largest:
                third_largest = second_largest
                second_largest = largest
                largest = n
            elif n > second_largest and n != largest:
                third_largest = second_largest
                second_largest = n
            elif n > third_largest and n != second_largest and n != largest:
                third_largest = n

        return largest if third_largest == float('-inf') else third_largest

obj = Solution()
print(obj.thirdMax([3,2,1]))
print(obj.thirdMax([2,2,3,1]))
print(obj.thirdMax([1,2]))

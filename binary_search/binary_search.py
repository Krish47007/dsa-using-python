def binary_search(nums,target):

    beg,end = 0,len(nums) - 1

    while beg <= end:
        mid = beg + (end - beg) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            beg = mid + 1

    return -1

print(binary_search([1,4,6,7,9],60))
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

# my solution
def findIndex(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif target < nums[m]:
            r = m - 1
        else:
            l = m + 1

    return -1


def searchRange(nums, target):
    if len(nums) == 0 or target < nums[0] or target > nums[len(nums) - 1]:
        return [-1, -1]

    index = findIndex(nums, target)
    if index == -1:
        return [-1, -1]
    else:
        l, r = 0, 0
        lIndex = index
        while True:
            if nums[lIndex - 1] != target or lIndex == 0:
                l = lIndex
                break
            else:
                lIndex -= 1

        while True:
            if index == len(nums) - 1 or nums[index + 1] != target:
                r = index
                break
            else:
                index += 1

        return [l, r]



nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))


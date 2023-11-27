'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

# my version
def searchInsert(self, nums, target):
    left = 0
    right = len(nums) - 1
    if target > nums[right]:
        return len(nums)
    elif target < nums[left]:
        return 0

    while left <= right:
        middle = (left + right) // 2 
        if nums[middle] == target:
            return middle
        elif target < nums[middle]:
            right = middle
            if left + 1 == middle:
                if nums[left] == target:
                    return left
                return middle
        else:
            left = middle
            if middle + 1 == right:
                return right
        
    return -1


# 
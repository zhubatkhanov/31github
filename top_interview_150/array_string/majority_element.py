"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

### 1st one line solution
# def majorityElement(nums):
#     nums.sort()
#     return nums[len(nums) // 2]

### 2nd solution
def majorityElement(nums):
    nums.sort()
    count = 0
    for i in range(len(nums)):
        count += 1
        if i+1 != len(nums) and nums[i+1] != nums[i]:
            if count > len(nums) // 2:
                return nums[i]
            count = 0
    
    return nums[len(nums) - 2]

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""


##### мое первое решение (Time Limit Exceeded - ошибка по времени)
# def rotate(nums, k):
#     if k > len(nums):
#         k = k % len(nums)
#
#     if k == len(nums):
#         return nums
#
#     while k > 0:
#         temp = nums[len(nums) - 1]
#         for i in range((len(nums)-2), -1, -1):
#             nums[i+1] = nums[i]
#
#         nums[0] = temp
#         k -= 1
#
#     return nums


### второе мое решение, у меня работает, но на платформе не работает
# def rotate(nums, k):
#     if k > len(nums):
#         k = k % len(nums)
#
#     if k == len(nums) or k == 0:
#         return nums
#
#     length = len(nums)
#     temp1 = nums[:length-k]
#     temp2 = nums[length-k:]
#     return temp2 + temp1


### 3ое решение, посмотрел готовое решение
# def rotate(nums, k):
#     k = k % len(nums)
#
#     if k == len(nums) or k == 0:
#         return nums
#
#     reverse(nums, 0, len(nums)-1)
#     reverse(nums, 0, k-1)
#     reverse(nums, k, len(nums)-1)
#     return nums
#
# def reverse(nums, start, end):
#     while start < end:
#         temp = nums[start]
#         nums[start] = nums[end]
#         nums[end] = temp
#         start += 1
#         end -= 1
#
#     return nums

def rotate(nums, k):
    k = k % len(nums)

    if k == len(nums) or k == 0:
        return nums

    result = [0] * len(nums)

    for i in range(len(nums)):
        index = (i+k) % (len(nums))
        result[index] = nums[i]

    return result





nums = [1,2,3,4,5,6,7]
print(rotate(nums, 3))
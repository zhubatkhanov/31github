"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that
should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""


# my solution
def merge(nums1, m, nums2, n):
    if m == 0:
        nums1 = nums2
    elif n != 0:
        first = m - 1
        second = n - 1
        index = m + n - 1
        while index >= 0 and first >= 0 and second >= 0:
            if nums1[first] < nums2[second]:
                nums1[index] = nums2[second]
                second -= 1
            else:
                nums1[index] = nums1[first]
                first -= 1
            index -= 1

        if index != -1:
            while index >= 0:
                if first < 0:
                    nums1[index] = nums2[second]
                    second -= 1
                else:
                    nums1[index] = nums1[first]
                    first -= 1
                index -= 1

    print(nums1)


nums1 = [2,0]
m = 1
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
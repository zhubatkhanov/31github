"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""

def strStr(haystack, needle):

    slow = 0
    lenNeed = len(needle)
    while slow < len(haystack):
        if haystack[slow] == needle[0]:
            if needle == haystack[slow:slow+lenNeed]:
                return slow
        slow += 1

    return -1



haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))
"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
"""
def isSubsequence(s,t):
    if len(t) < len(s):
        return False
    if len(s) == 0:
        return True

    count = 0
    for i in t:
        if s[count] == i:
            count += 1
            if count == len(s):
                return True

    return False


s = "abc"
t = "atbsca"

print(isSubsequence(s, t))
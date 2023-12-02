"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

def isPalindrome(s):
    if s == " " or s == "":
        return True
    s = s.lower()

    left, right = 0, len(s) - 1
    while left < right:
        if s[left].isalnum() == False:
            left += 1
            continue

        if s[right].isalnum() == False:
            right -= 1
            continue

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

print(isPalindrome(".,"))
"""
744. Find Smallest Letter Greater Than Target

Companies
You are given an array of characters letters that is sorted in non-decreasing order,
 and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target.
If such a character does not exist, return the first character in letters.


Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

"""


""""   leetcode solution 
def nextGreatestLetter(letters, target):

    left, right = 0, len(letters) - 1
    
    if target < letters[0] or target >= letters[right]:
        return letters[0]

    while left <= right:

        mid = (left + right)//2

        if target < letters[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return letters[left]

"""

# my solution
def nextGreatestLetter(letters, target):
    if target < letters[0] or target > letters[len(letters) - 1] or target == letters[len(letters) - 1]:
        return letters[0]

    letters = set(letters)
    letters = sorted(list(letters))
    left, right = 0, len(letters) - 1

    while left <= right:
        mid = (left + right) // 2

        if right - left == 1:
            return letters[right]

        if letters[mid] == target:
            return letters[mid + 1]
        elif target > letters[mid]:
            left = mid
        else:
            right = mid






letters = ["e","e","e","e","e","e","n","n","n","n"]
target = "e"
print(nextGreatestLetter(letters, target))

"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
from collections import defaultdict

# first solution
def canConstruct(ransomNote, magazine):
    letters_count_magazine = defaultdict(int)
    letters_count_ransom = defaultdict(int)
    for char in magazine:
        letters_count_magazine[char] += 1

    for char in ransomNote:
        letters_count_ransom[char] += 1

    for key,value in letters_count_ransom.items():
        if letters_count_magazine[key] < value:
            return False

    print(letters_count_ransom.values())
    return True



ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))
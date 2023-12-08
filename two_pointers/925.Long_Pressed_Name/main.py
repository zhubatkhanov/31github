"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c,
the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name,
with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
"""
# optimize solution
# def isLongPressedName(name, typed):
#     i, j = 0, 0
#
#     while j < len(typed):
#         if i < len(name) and name[i] == typed[j]:
#             i += 1
#             j += 1
#         elif j > 0 and typed[j] == typed[j - 1]:
#             j += 1
#         else:
#             return False
#
#     return i == len(name)


# my solution :)
def isLongPressedName(name, typed):
    first, second = 0, 0
    if name[first] != typed[first]:
        return False

    while first < len(name):
        if name[first] == typed[second]:
            first += 1
        else:
            if first != 0:
                if typed[second] != name[first - 1]:
                    return False
        second += 1

        if second == len(typed) and first != len(name):
            return False

    while second < len(typed):
        if typed[second] != name[first - 1]:
            return False
        second += 1

    return True


name = "alex"
typed = "aaxleex"
print(isLongPressedName(name, typed))
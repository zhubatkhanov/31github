

def reverseVowels(s):
    vowels = "aeiouAEIOU"
    left, right = 0, len(s) - 1
    leftCheck, rightCheck = False, False
    s = list(s)
    while left < right:
        if vowels.find(s[left]) != -1:
            leftCheck = True

        if vowels.find(s[right]) != -1:
            rightCheck = True

        if leftCheck and rightCheck:
            leftCheck = False
            rightCheck = False
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

        if leftCheck and rightCheck == False:
            right -= 1
        elif rightCheck and leftCheck == False:
            left += 1
        else:
            left += 1
            right -= 1

    return str(s)


print(reverseVowels("hello"))
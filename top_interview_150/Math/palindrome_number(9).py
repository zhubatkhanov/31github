

def isPalindrome(x):
    inputNum = x
    newNum = 0
    while x > 0:
        newNum = (newNum * 10) + (x % 10)
        x = x // 10

    return inputNum == newNum



print(isPalindrome(121))
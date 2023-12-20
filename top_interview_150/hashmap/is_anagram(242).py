from collections import defaultdict

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    dictS = defaultdict(int)
    dictT = defaultdict(int)

    for i in range(len(s)):
        dictS[s[i]] += 1
        dictT[t[i]] += 1

    return dictS == dictT


s = "rat"
t = "car"
print(isAnagram(s, t))
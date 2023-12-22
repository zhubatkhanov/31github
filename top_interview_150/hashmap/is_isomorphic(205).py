from collections import defaultdict

def isIsomorphic(s, t):
    dict = defaultdict(str)

    for i in range(len(s)):
        if s[i] in dict:
            if dict[s[i]] != t[i]:
                return False
            continue

        if t[i] in dict.values():
            return False
        dict[s[i]] = t[i]

    return True


s = "badc"
t = "baba"
print(isIsomorphic(s, t))
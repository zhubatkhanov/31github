from collections import defaultdict
def wordPattern(pattern, s):
    words = s.split(" ")
    patternDict = defaultdict(str)

    for i in range(len(pattern)):
        if pattern[i] in patternDict:
            if patternDict[pattern[i]] != words[i]:
                return False
        else:
            if words[i] in patternDict.values():
                return False
            patternDict[pattern[i]] = words[i]

    return True



pattern = "abba"
s = "dog dog cat dog"

print(wordPattern(pattern, s))
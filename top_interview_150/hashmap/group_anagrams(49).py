from collections import defaultdict
def groupAnagrams(strs):

    dict = defaultdict(list)

    for s in strs:
        dict[tuple(sorted(s))].append(s)

    return dict.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))


from collections import defaultdict

def groupAnagrams(strs):

    groups = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
        

    return list(groups)

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
















































'''
from collections import defaultdict

def groupAnagrams(strs):

    groups = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())
    
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
'''
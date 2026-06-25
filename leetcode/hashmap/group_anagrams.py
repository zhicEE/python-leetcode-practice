# LeetCode 49 - Group Anagrams
# word → key → groups[key].append(word)

from collections import defaultdict 

def groupAnagrams(strs):
    groups = defaultdict(list) # auto-creates empty list for new keys

    for word in strs:
        key = "".join(sorted(word)) # join turns list into string key
        groups[key].append(word)
    return list(groups.values())
    
if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
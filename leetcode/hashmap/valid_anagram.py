# LeetCode 242 - Valid Anagram

# manual test
s = "anagram"
t = "nagaram"

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

for ch in t:
    count[ch] = count.get(ch, 0) - 1

for value in count.values():
    if value != 0:
        print(False)
        break
else:
    print(True)


# function solution
def isAnagram(s, t):

    if len(s) != len(t):
        return False

    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1 

    for ch in t:
        count[ch] = count.get(ch, 0) - 1

    for v in count.values():
        if v != 0:
            return False
        
    return True

# test
if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))
    print(isAnagram("rat", "car"))
# A. Get a value from a dictionary
ages = {
    "Alice": 20,
    "Bob": 21
}
print(ages["Bob"])

# B. Add a new key-value pair to a dictionary
ages["Charlie"] = 19
print(ages)

# C1. Check duplicates - my original solution
nums = [1, 2, 3, 2]
seen = set()
for i in nums:
    for j in seen:
        if i == j:
            print("True")
    seen.add(i)

# C2. Check duplicates - improved solution
nums = [1, 2, 3, 2]
seen = set()
has_duplicate = False
for num in nums:
    if num in seen:
        has_duplicate = True
        break
    seen.add(num)
print(has_duplicate)

# D. Count how many times each number appears
counts = {}
nums = [1, 2, 2, 3, 3, 3]
for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
print(counts)
# A
for i in range(1, 11):
    print(i)

# B
for i in range(1, 21):
    if i % 2 != 0:
        print(i)

# C
total = 0
for i in range(1, 101):
    total += i
print(total)

# D
nums = [8, 3, 10, 1, 6]
min_num = nums[0]

for num in nums:
    if num < min_num:
        min_num = num

print(min_num)

# E
nums = [8, 3, 10, 1, 6]
count = 0

for num in nums:
    if num > 5:
        count += 1

print(count)

# F
nums = [2, 4, 6]

for num in nums:
    print(num * 2)
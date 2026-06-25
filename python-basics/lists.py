# A
nums = [10, 20, 30]
for i, num in enumerate(nums):
    print(i, num)

# B
nums = [1, 2, 3, 4, 5, 6]
evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)
print(evens)

# C
nums = [1, 2, 3]
doubled = []
for num in nums:
    num = num * 2
    doubled.append(num)
print(doubled)

# D
nums = [10, 20, 30]
nums[1] = 99
print(nums)

# E
nums = [1, 3, 4, 8, 10]
for i in nums:
    if i > 5:
        print(i)
        break
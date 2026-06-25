nums = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(nums):

    need = target - num

    if need in seen:
        print(seen[need], i)
        break

    seen[num] = i
# LeetCode 1 - Two Sum
"""
Difficulty:
Easy

Pattern:
Hash Map

Key idea:
- Traverse the array once.
- For each number, calculate its complement: target - number.
- Use a hash map to check whether the complement was seen before.
- Store each number with its index.

Complexity:
Time: O(n)
Space: O(n)
"""

nums = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(nums):

    need = target - num

    if need in seen:
        print(seen[need], i)
        break

    seen[num] = i

# 2026-07-26 Review
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        seen = {}

        for index, num in enumerate(nums):

            needed = target - num

            if needed in seen:
                return [seen[needed], index]

            seen[num] = index
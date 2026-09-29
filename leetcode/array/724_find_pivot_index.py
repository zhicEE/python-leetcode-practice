# LeetCode 724 - Find Pivot Index
"""
Difficulty:
Easy

Pattern:
Brute Force

Key idea:
- Try each index as the pivot from left to right.
- Sum the elements strictly to its left and strictly to its right.
- Return the first index whose left and right sums match.
- Return -1 if no pivot exists.

Complexity:
Time: O(n^2)
Space: O(1)
"""

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for pivot in range(len(nums)):
            left_sum = 0
            right_sum = 0

            for left_index in range(pivot):
                left_sum += nums[left_index]

            for right_index in range(pivot + 1, len(nums)):
                right_sum += nums[right_index]

            if left_sum == right_sum:
                return pivot

        return -1

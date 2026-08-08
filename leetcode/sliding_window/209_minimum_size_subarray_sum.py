# LeetCode 209 - Minimum Size Subarray Sum
"""
Difficulty:
Medium

Pattern:
Variable-Size Sliding Window

Key idea:
- Expand the window by moving the right pointer and adding nums[right].
- When the window sum is greater than or equal to target, the window is valid.
- Record the minimum valid window length.
- Shrink the window from the left while it remains valid.
- Positive elements guarantee that expanding increases the sum and shrinking decreases it.
- Return 0 if no valid subarray exists.

Complexity:
Time: O(n)
Space: O(1)
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        window_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_length = min(
                    min_length,
                    right - left + 1
                )

                window_sum -= nums[left]
                left += 1

        if min_length == float("inf"):
            return 0

        return min_length
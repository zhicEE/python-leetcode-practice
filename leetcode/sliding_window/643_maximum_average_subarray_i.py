# LeetCode 643 - Maximum Average Subarray I
"""
Difficulty:
Easy

Pattern:
Sliding Window

Key idea:
- Use a fixed-size sliding window of length k.
- Calculate the sum of the first window as the initial state.
- Move the window by removing the left element and adding the new right element.
- Track the maximum window sum instead of recalculating every subarray.
- Convert the maximum sum to average at the end.

Complexity:
Time: O(n)
Space: O(1)
"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]

            max_sum = max(max_sum, window_sum)

        return max_sum / k
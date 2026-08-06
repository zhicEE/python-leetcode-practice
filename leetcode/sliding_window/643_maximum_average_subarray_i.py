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


# 2026-08-03 Review
def findMaxAverage(nums: list[int], k: int) -> float:
	current_sum = sum(nums[:k])
	max_sum = current_sum

	for i in range (k, len(nums)):
		current_sum = current_sum - nums[i - k] + nums[i]
		max_sum = max(max_sum, current_sum)
	
	return max_sum / k
"""
Review result:
- Correctly identified this as a fixed-size sliding window problem.
- Understood that the window should remove nums[i - k] and add nums[i].
- Could explain why the solution is O(n).

Mistakes:
- Wrote sum(:k) instead of sum(nums[:k]).
- Forgot the parentheses in range(...).
- Used the wrong loop range.
- Did not remember that i represents the index of the new element entering the window.

Key reminder:
- Initialize the first window with nums[:k].
- Start the loop from i = k.
- nums[i] enters the window.
- nums[i - k] leaves the window.

Main error type:
- Python syntax / structure
- Loop boundary
"""

# 2026-08-06 Review
def findMaxAverage(nums: list[int], k: int) -> float:
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
         window_sum = window_sum + nums[i] - nums[i-k]
         max_sum = max(max_sum, window_sum)

    return max_sum / k
# LeetCode 167 - Two Sum II - Input Array Is Sorted
"""
Pattern:
Two Pointers

Key idea:
- Use two pointers because the array is sorted.
- Move left pointer when sum is too small.
- Move right pointer when sum is too large.
- Each step eliminates impossible pairs.

Complexity:
Time: O(n)
Space: O(1)
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            elif current_sum < target:
                left += 1

            else:
                right -= 1


"""
Mistake Note:
1. Wrong approach:
   - Tried to use two separate while loops:
     
        while sum < target:
            left += 1

        while sum > target:
            right -= 1

   - Problem:
     Adjusting one pointer can make the sum cross the target.
     The other pointer may need to be adjusted again.
     Two pointers should update step by step inside one loop.

2. Index mistake:
   - The problem requires 1-indexed positions.
   - Python uses 0-indexed positions.
   - Return [left + 1, right + 1].
"""
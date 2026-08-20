# LeetCode 704 - Binary Search
"""
Difficulty:
Easy

Pattern:
Binary Search

Key idea:
- The array is sorted in ascending order.
- Maintain an inclusive search range [left, right].
- Calculate the middle index and compare nums[mid] with target.
- If nums[mid] equals target, return mid.
- If nums[mid] is smaller than target, search the right half by setting left = mid + 1.
- If nums[mid] is greater than target, search the left half by setting right = mid - 1.
- Continue while left <= right because a single-element range is still valid.
- Return -1 if the target does not exist.

Complexity:
Time: O(log n)
Space: O(1)
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# 2026-08-18 Review
def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1
    # Mistakes:
    # - Initially confused time complexity with O(n).
    # - Need to distinguish execution steps from extra space.


# 2026-08-20 Review
# Mistake:
# - Used len(nums) instead of len(nums)-1
# - Confused search condition with value comparison
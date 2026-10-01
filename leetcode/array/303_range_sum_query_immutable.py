# LeetCode 303 - Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/
"""
Difficulty:
Easy

Pattern:
Direct Range Traversal (NumArrayBruteForce)

Key idea:
- Store a reference to the input array during initialization.
- For each query, visit every index from left through right, inclusive.
- Accumulate the values and return the total.

Complexity:
Initialization: O(1) time and O(1) extra space; the array is not copied.
Each query: O(right - left + 1) time, O(n) in the worst case.
Extra space per query: O(1).
"""


class NumArrayBruteForce:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        total = 0

        for i in range(left, right + 1):
            total += self.nums[i]

        return total


class NumArray:
    """Prefix Sum approach for repeated queries on an unchanged array.

    prefix[i] stores the sum of the first i elements; prefix[0] is 0.
    Inclusive range [left, right]: prefix[right + 1] - prefix[left].
    Initialization: O(n) time.
    Each query: O(1) time and O(1) additional working space.
    Total extra space: O(n) for the n + 1 stored prefix sums.
    """

    def __init__(self, nums: list[int]):
        self.prefix = [0]

        for num in nums:
            next_sum = self.prefix[-1] + num
            self.prefix.append(next_sum)

    def sumRange(self, left: int, right: int) -> int:
        total = self.prefix[right + 1] - self.prefix[left]

        return total


# 2026-10-01 Initial Attempt
# Key mistakes: Excluded the right endpoint; summed prefix entries instead of subtracting two values; confused local prefix with self.prefix; reused the class name; omitted stored prefix sums from total extra space.

# LeetCode 3 - Longest Substring Without Repeating Characters
"""
Difficulty:
Medium

Pattern:
Sliding Window

Key idea:
- Use a variable-size sliding window.
- Use a set to store the characters currently inside the window.
- Expand the window by moving the right pointer.
- If the new character already exists in the window, move the left
  pointer and remove characters until the duplicate disappears.
- Track the maximum valid window length.

Complexity:
Time: O(n)
Space: O(min(n, k)), where k is the size of the character set
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        left = 0
        max_length = 0

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length
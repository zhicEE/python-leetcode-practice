# LeetCode 11 - Container With Most Water
"""
Pattern:
Two Pointers

Key idea:
- Start with two pointers at the widest possible container.
- Calculate the area using the shorter line as the height.
- Move the pointer at the shorter line inward.
- Only a taller line can offset the reduced width and produce a larger area.

Complexity:
Time: O(n)
Space: O(1)
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:

            area = min(height[left], height[right]) * (right - left)
            
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

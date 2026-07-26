# Leetcode 20 - Valid Parentheses
"""
Difficulty:
Easy

Pattern:
Stack

Key idea:
- Push each opening bracket onto the stack.
- When a closing bracket appears, check whether it matches the top of the stack.
- Return False if the stack is empty or the brackets do not match.
- After processing all characters, the stack must be empty.

Complexity:
Time: O(n)
Space: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack.pop() != matching[char]:
                    return False

        return not stack
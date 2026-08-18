# LeetCode 206 - Reverse Linked List
"""
Difficulty:
Easy

Pattern:
Linked List

Key idea:
- Reverse the direction of pointers in a linked list.
- Use three pointers: previous, current, and next.
- Move through the list while updating each node's next pointer.
- Return the new head after reversing the linked list.

Complexity:
Time: O(n)
Space: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous = None
        current = head

        while current:
            next_node = current.next # save next node

            current.next = previous # reverse pointer

            previous = current
            current = next_node # move forward

        return previous
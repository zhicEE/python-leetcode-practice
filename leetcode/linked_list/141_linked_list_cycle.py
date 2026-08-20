# LeetCode 141 - Linked List Cycle
"""
Difficulty:
Easy

Pattern:
Linked List / Fast & Slow Pointers

Key idea:
- Use two pointers with different speeds to detect a cycle.
- Move slow one step and fast two steps at a time.
- If a cycle exists, fast will eventually catch slow inside the cycle.
- If fast reaches None, the linked list does not contain a cycle.
- Use O(1) extra space instead of storing visited nodes.

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
   def hasCycle(self, head: Optional[ListNode]) -> bool:

      slow = head
      fast = head

      while fast and fast.next:

         slow = slow.next
         fast = fast.next.next

         if fast == slow:
            return True

      return False
            
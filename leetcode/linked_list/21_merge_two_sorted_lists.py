# LeetCode 21 - Merge Two Sorted Lists
"""
Difficulty:
Easy

Pattern:
Linked List / Two Pointers

Learning goals:
- Compare the current nodes of two sorted linked lists.
- Build the merged list with a dummy node and a tail pointer.
- Append the remaining nodes after one list is exhausted.

Key idea:
- Compare list1.val and list2.val while both current nodes exist.
- Connect the smaller current node to tail, advance only its source list,
  and then move tail to the newly connected node.
- When one list is exhausted, connect the other sorted remainder directly.
- Return dummy.next because dummy is only a temporary head node.

Complexity:
Time: O(n + m)
Space: O(1)

Observed mistake:
- Initially confused changing tail.next with moving tail. Setting tail.next
  connects a node; assigning tail = tail.next moves the tail pointer.
- In the 2026-09-04 review, the first attempt used `List.Node`, did not advance
  the selected source-list pointer, and placed the tail movement outside the
  loop. These were corrected after targeted hints.

Review history:
- 2026-08-27: Closed-book rewrite passed ordinary, one-empty, and both-empty
  cases. The pointer explanation and time complexity were corrected during
  review.
- 2026-09-04: The corrected closed-book rewrite passed ordinary, one-empty,
  and both-empty cases. The user then correctly distinguished changing the
  link from moving `tail` and gave O(n + m) time and O(1) additional space.

Next review:
2026-09-05

Similar problem:
LeetCode 23 - Merge k Sorted Lists
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        tail.next = list1 or list2

        return dummy.next


# 2026-08-27 Review
def merge_two_lists_review(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    tail.next = list1 or list2

    return dummy.next


# 2026-09-04 Review
def merge_two_lists_review_2(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val > list2.val:
            tail.next = list2
            list2 = list2.next
        else:
            tail.next = list1
            list1 = list1.next

        tail = tail.next

    tail.next = list1 or list2

    return dummy.next


# 2026-09-06 Review
def merge_two_lists_review_3(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:

        if list1.val > list2.val:
            tail.next = list2
            list2 = list2.next
        else:
            tail.next = list1
            list1 = list1.next

        tail = tail.next

    tail.next = list1 or list2

    return dummy.next
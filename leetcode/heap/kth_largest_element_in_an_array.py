# LeetCode 215 - Kth Largest Element in an Array

# A heap always keeps the smallest number at the first position.

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap [0]
    
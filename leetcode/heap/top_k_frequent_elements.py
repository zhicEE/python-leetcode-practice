# LeetCode 347 - Top K Frequent Elements

# A
from collections import Counter
import heapq

nums = [1, 1, 1, 2, 2, 3]
k = 2

count = Counter(nums)

heap = []

for num, freq in count.items():
    heapq.heappush(heap, (freq, num))

    if len(heap) > k:
        heapq.heappop(heap)
 
result = [num for freq, num in heap]

print("Top K Frequent Elements:", result)


# B
# First, count the frequency. Then sort the pairs of (number, frequency) by frequency from highest to lowest. Finally, take the first k numbers.
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        items = list(count.items())
        items.sort(key=lambda x: x[1], reverse = True)
        return [num for num, freq in items[:k]]
    
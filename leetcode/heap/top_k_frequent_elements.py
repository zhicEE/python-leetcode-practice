# LeetCode 347 - Top K Frequent Elements

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
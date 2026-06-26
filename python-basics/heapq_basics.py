
# tuple + print
x = (3, "a")

print(x)
print(x[0])
print(x[1])


# unpacking
a, b = (5, "apple")

print(a)
print(b)


# for + unpacking
pairs = [(1, "x"), (2, "y"), (3, "z")]

for a, b in pairs:
    print(a, b)

# list comprehension
nums = [1, 2, 3, 4]
res = [x * 2 for x in nums]

print(res)


pairs = [(3, "a"), (1, "b"), (5, "c")]
res = [b for a, b in pairs]

print(res)


# heap
import heapq

heap = []

heapq.heappush(heap, (3, "a"))
heapq.heappush(heap, (1, "b"))
heapq.heappush(heap, (5, "c"))

print(heap)


# pop
print(heapq.heappop(heap))
print(heap)
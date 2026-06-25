def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

#test
print(containsDuplicate([1, 2, 3, 1]))
def find_duplicate(nums):
    nums.sort()  # Sort the array in-place

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]

# Example
arr = [1, 3, 4, 2, 2]
result = find_duplicate(arr)
print("Duplicate number in the array:", result)
# achieve this O(n log n)

# with out using sort method we cant get nlogn the traditionalway will give you O(n) 
# because we have to check n numbers

def find_duplicate(nums):
    # Initialize the pointers
    tortoise = nums[0]
    hare = nums[0]

    # Phase 1: Find the intersection point
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Phase 2: Find the duplicate number
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return tortoise

# Example
arr = [1, 3, 4, 2, 2]
result = find_duplicate(arr)
print("Duplicate number in the array:", result)


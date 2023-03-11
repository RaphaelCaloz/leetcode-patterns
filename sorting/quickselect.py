
# NOTE: Returns the element that would be at position k within
# the list if it were sorted, with indexing STARTING AT ZERO.
# DOES NOT return the the kth smallest 
# of the distinct values in the list.

# For example, if called with k=2, even though the 3rd smallest 
# distinct value in [1, 1, 1, 2, 3] is 3, 
# the third "1" element will be returned, as it is the third element
# in the sorted list, starting from the left.

# See detailed explanation here: https://stackoverflow.com/questions/14268693/quick-select-with-repeat-values

# Time complexity:
# --- Average: O(n)
# --- Worst:   O(n^2)
def quick_select(nums, k, l, r):
    # Init pivot and p
    pivot, p = nums[r], l

    # Partition nums
    for i in range(l, r):
        if nums[i] < pivot:
            nums[p], nums[i] = nums[i], nums[p]
            p += 1
        
    # Place pivot in its final position in the sorted array
    nums[r], nums[p] = nums[p], nums[r]

    # Recurse left/right, or return, depending on p and k
    if p > k: return quick_select(nums, k, l, p-1)
    if p < k: return quick_select(nums, k, p+1, r)
    return nums[p]

# Usage (the following code is not part of the template):
my_nums = [1,3,2,0]
k = 2  # Should return 2
result = quick_select(my_nums, k, 0, 3)
print(result)
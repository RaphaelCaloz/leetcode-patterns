from random import randint

def quick_sort(nums, l, r):
    # End recursion
    if l >= r: 
        return

    # Pick random pivot and init p
    pivot_idx = randint(l, r)
    nums[r], nums[pivot_idx] = nums[pivot_idx], nums[r]
    pivot, p = nums[r], l

    # Partition nums
    for i in range(l, r):
        if nums[i] < pivot:
            nums[p], nums[i] = nums[i], nums[p]
            p += 1
        
    # Place pivot in its final position in the sorted array
    nums[r], nums[p] = nums[p], nums[r]

    # Recurse left and right
    quick_sort(nums, l, p-1)
    quick_sort(nums, p+1, r)

# Usage (the following code is not part of the template):
my_nums = [2,0,1,3,4,6,7,19,10,6]
quick_sort(my_nums,0, len(my_nums)-1)
print(my_nums)
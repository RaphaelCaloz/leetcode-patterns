# Suppose we have a search space. It could be an array, a range, etc. Usually it's sorted in ascending order. 
# Reduce problem to:
# 'Minimize k , s.t. condition(k) is True',
# then apply the following template.

# The following code is the most generalized binary search template:
def binary_search(array):
    def condition(value):
        pass

    lo, hi = min(search_space), max(search_space)  # could be [0, n], [1, n] etc. Depends on problem
    while lo < hi:
        mid = (hi + lo)//2
        if condition(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo  # Replace by lo-1 depending on problem

# What's really nice of this template is that, for most of the binary search problems, 
# we only need to modify three parts after copy-pasting this template, and never need to worry about corner cases and bugs in code any more:

# 1. Correctly initialize the boundary variables lo and hi to specify search space. Only one rule: set up the boundary to include all possible elements;
# 2. Decide return value. Is it return lo or return lo - 1? Remember this: after exiting the while loop, lo is the minimal k​ satisfying the condition function;
# 3. Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.

# NOTE: Often are the situations where the search space and search target are not so readily available...
# ...so when to consider using binary search? 
# If we can discover some kind of monotonicity, for example, 
# if condition(k) is True then condition(k + 1) is True, 
# then we can consider binary search.

# NOTE: for more info, visit: https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
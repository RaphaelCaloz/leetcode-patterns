# Not really a template, just an example
# of solution (question: course schedule)
# that is very close to a template.

# Pseudocode
# # parent initialized as (x -> x)
# def find(x):
#     while parent[x] != x: #While x isn't the leader
#         x = parent[x]
#     return x

# def union(x, y):
#     parent[find(x)] = find(y)


# NOTE: Identify if problems talks about finding groups or components.
# # Simpler, non-optimized version
# class DSU:
#     def __init__(self):
#         self.par = range(1001)
#     def find(self, x):
#         if self.par[x] != x:
#             self.par[x] = self.find(self.par[x])
#         return self.par[x]
#     def union(self, x, y):
#         self.par[self.find(x)] = self.find(y)
# Optimized DSU using Union-By-Rank and path contraction
class DSU:
    def __init__(self, n):
        # Init parents and rank iterables
        self.par = [i for i in range(n)]
        self.rnk = [0 for _ in range(n)]

    def find(self, x):
        # Go up parents recursively and contract paths
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        # Find parents of x and y
        xr, yr = self.find(x), self.find(y)
        # If same parents, return False
        if xr == yr:
            return False
        # Else, compare their ranks to assign their parents
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution:
    def LCQuestion(self, edges, n):  # If no "n" param, try setting n to max of problem + 1
        # Build dsu from input
        d = DSU(n)
        for edge in edges:
            if condition(edge):  # Might not need condition
                if not d.union(*edge):
                    # return/count/process something    
                    pass    
        # Further processing
        # Ex.: Count connected components:
        # connected_comps = n
        # for i, p in enumerate(d.par):
        #     if i != p:
        #         connected_comps -= 1
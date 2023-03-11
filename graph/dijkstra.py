class Solution:
    def networkDelayTime(self, times, n, k):
        # Create adjacency list
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((w, v))

        # Init var/DS
        min_heap = [(0, k)]
        visit = set()  # To avoid going in a cycle
        t =  0  # Cost to reach last node

        # Dijkstra's algorithm
        while min_heap:
            # Pop from heap
            w1, n1 = heapq.heappop(min_heap)

            # Avoid going through all of n1's neighbors
            # if it has already been visited.
            if n1 in visit:
                continue

            # Visit n1
            visit.add(n1)
            t = w1

            # BFS through neighbors of n1
            for w2, n2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(min_heap, (w1+w2, n2))
        return t if len(visit) == n else -1
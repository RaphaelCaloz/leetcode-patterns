class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        
        # Compute distances
        adj = [[] for i in range(N)]
        for i in range(N):
            for j in range(i+1, N):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                adj[i].append([dist, j])
                adj[j].append([dist, i])
                
        # Prim's algorithm
        res = 0
        minH = [[0,0]]
        visited = set()
        
        while len(visited) < N:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minH, [neiCost, nei])
            visited.add(i)
            res += cost
        return res
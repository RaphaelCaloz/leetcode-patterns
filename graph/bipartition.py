from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.N = len(graph)
        # -1: Uncolored
        # 0: Red
        # 1: Green
        self.colors = [-1]*self.N
        self.graph = graph
        
        for i in range(self.N):
            if self.colors[i] == -1:
                if not self.isBipartiteUtil(i):
                    return False
        return True
    
    
    # This function returns true if graph G[V][V]
    # is Bipartite, else false
    def isBipartiteUtil(self, src):
        q = deque()
        q.append(src)
        self.colors[src] = 0

        while q:
            cur = q.popleft()
            for node in self.graph[cur]:  # For every node adjacent to cur
                # If adjacent node has same color as cur
                if self.colors[node] == self.colors[cur]: 
                    return False
                # If node is uncolored, color it with opposite color as cur
                elif self.colors[node] == -1:
                    q.append(node)
                    self.colors[node] = 1-self.colors[cur] 
        return True
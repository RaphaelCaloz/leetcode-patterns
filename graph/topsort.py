# NOTE: edges are [v1, v2], as in v1->v2
def topsort(vertex_count, edges):
    # Init DS
    adj = [[] for i in range(vertex_count)]
    deg = [0 for _ in range(vertex_count)]
    sorted_list = []

    # Build adj list and in degree list
    for v1, v2 in edges:
        adj[v1].append(v2)
        deg[v2] += 1
    
    # Find all sources (nodes with in degree of 0), add them to queue
    q = deque()
    for vertex, d in enumerate(deg):
        if d == 0:
            q.append(vertex)
    
    # For every source:
    # 1. Add it to sorted list
    # 2. Decrement degree of its children
    # 3. If child now has in degree of 0, add it to queue
    while q:
        cur = q.popleft()
        sorted_list.append(cur)
        for child in adj[cur]:
            deg[child] -= 1
            if deg[child] == 0:
                q.append(child)
    return sorted_list  # or return len(sorted_list) == vertex_count, if the question is to check whether a valid sorting exists
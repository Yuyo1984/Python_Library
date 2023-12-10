from heapq import heapify, heappush, heappop

# トポロジカルソート（辞書順最小）
def topological_sort(graph):
    count = [0] * len(graph)
    for nodes in graph:
        for u in nodes:
            count[u] += 1
    
    pq = [i for i, cnt in enumerate(count) if cnt == 0]
    heapify(pq)
    
    topological_sorted = []
    visited = set(pq)
    
    while pq:
        now = heappop(pq)
        topological_sorted.append(now)
        
        for next in graph[now]:
            if next in visited:
                continue
            
            count[next] -= 1
            
            if count[next] <= 0:
                visited.add(next)
                heappush(pq, next)
    
    if len(topological_sorted) == len(graph):
        return topological_sorted
    else:
        return None

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = [[] for _ in range(n)]
        for u,v,c in edges:
            adj[u].append((c,v))
        
        L = [(0,src)]
        dist = {i:-1 for i in range(n)}
        while L:
            total_cost, node = heapq.heappop(L)
            if dist[node] !=-1:
                continue
            dist[node] = total_cost
            for (weight,neighbor) in adj[node]:
                if dist[neighbor] ==-1:
                    heapq.heappush(L, (total_cost+weight, neighbor))
        return dist



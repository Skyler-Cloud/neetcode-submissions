class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        edge_dict = defaultdict(list)
        for u,v,c in edges:
            edge_dict[u].append((c,v))
        
        L = [(0,src)]
        out = {}
        while L:
            total_cost, node = heapq.heappop(L)
            if node in out:
                continue
            out[node] = total_cost
            for (weight,neighbor) in edge_dict[node]:
                if neighbor not in out:
                    heapq.heappush(L, (total_cost+weight, neighbor))
        for node in range(n):
            if node not in out:
                out[node]=-1
        return out


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph={}
        for i in range(n):
            graph[i]=[]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        visited=set()
        q=deque([source])
        visited.add(source)
        while q:
            node=q.popleft()
            if node==destination:
                return True
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return False
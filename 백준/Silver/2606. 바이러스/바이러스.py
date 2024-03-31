from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

infested = []

def bfs(v, visited):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        k = q.popleft()
        
        for i in graph[k]:
            if visited[i] == False:
                q.append(i)
                infested.append(i)
                visited[i] = True

bfs(1, visited)

print(len(infested))
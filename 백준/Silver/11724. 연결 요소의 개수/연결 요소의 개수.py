import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

def bfs(start, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)

result = 0
for i in range(1, n+1):
    if visited[i] == False:
        bfs(i, visited)
        result += 1

print(result)
import sys
from collections import deque

input = sys.stdin.readline

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]

for i in range(0, d):
    graph[i].append((i+1, 1))

for i in range(n):
    a, b, c = map(int, input().split())
    if b > d:
        continue
    graph[a].append((b, c))

visited = []
for i in range(d+1):
    visited.append(i)

def bfs(start):
    q = deque([start])

    while q:
        now = q.popleft()

        for v in graph[now]:
            visited[v[0]] = min(visited[v[0]], visited[now]+v[1])
            q.append(v[0])

bfs(0)
print(visited[d])
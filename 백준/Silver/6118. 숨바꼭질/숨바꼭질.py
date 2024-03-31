import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)

def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()

        for v in graph[now]:
            if visited[v] == 0:
                visited[v] = visited[now] + 1
                q.append(v)

bfs(1)
print(visited.index(max(visited)), end=" ")
print(max(visited) - 1, end=" ")

cnt = 0
for k in visited:
    if k == max(visited):
        cnt += 1
print(cnt)
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]

visited = [0] * (n + 1)
parent = [0] * (n + 1)

for i in range(1, n+1):
    parent[i] = i

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        v = q.popleft()

        for x in graph[v]:
            if visited[x] == 0:
                visited[x] = 1
                parent[x] = v
                q.append(x)

bfs(1)

for i in range(2, n+1):
    print(parent[i])
import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

c = 1
def bfs(start):
    global c
    q = deque([start])
    visited[start] = c

    while q:
        now = q.popleft()
        graph[now].sort()

        for v in graph[now]:
            if visited[v] == False:
                c += 1
                visited[v] = c
                q.append(v)

bfs(r)

for i in range(1, n+1):
    print(visited[i])
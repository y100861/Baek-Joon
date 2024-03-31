import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

array = [0] * (n + 1)

def bfs(start):
    c = 0
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        now = q.popleft()

        for v in graph[now]:
            if visited[v] == False:
                c += 1
                visited[v] = True
                q.append(v)

    array[start] = c

for i in range(1, len(graph)):
    bfs(i)

for i in range(1, len(array)):
    if array[i] == max(array):
        print(i, end=" ")
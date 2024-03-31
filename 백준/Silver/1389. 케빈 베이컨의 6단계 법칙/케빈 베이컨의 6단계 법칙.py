import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque([start])
    result = []
    visited = [0] * (n + 1)
    visited[start] = 1

    while q:
        now = q.popleft()

        for v in graph[now]:
            if visited[v] == 0:
                visited[v] = visited[now] + 1
                result.append(visited[v] - 1)
                q.append(v)

    return sum(result)

sum_num = []
for i in range(1, n+1):
    sum_num.append(bfs(i))

print(sum_num.index(min(sum_num)) + 1)
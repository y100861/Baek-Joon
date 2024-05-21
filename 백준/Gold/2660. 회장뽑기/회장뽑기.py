import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

while True:
    a, b = map(int, input().split())
    if (a, b) == (-1, -1):
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()

        for v in graph[now]:
            if visited[v] == 0:
                visited[v] = int(visited[now] + 1)
                q.append(v)

s = 0
num = []
result = 50
for i in range(1, n+1):
    visited = [0] * (n + 1)
    bfs(i)
    result = min(max(visited) - 1, result)

for i in range(1, n+1):
    visited = [0] * (n + 1)
    bfs(i)
    if max(visited)-1 == result:
        s += 1
        num.append(i)

print(result, s)

for n in num:
    print(n, end=" ")
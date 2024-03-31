import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

array = copy.deepcopy(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    graph[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 

            if not (0<=nx<n and 0<=ny<m):
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny))

for i in range(1):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i, j)

if array[n-1] != graph[n-1]:
    print("YES")
else:
    print("NO")
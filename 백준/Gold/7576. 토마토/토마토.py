import sys
import copy
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
visited = copy.deepcopy(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
           q.append((i, j)) 

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and graph[nx][ny] != -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

bfs()

for i in range(n):
    if 0 in visited[i]:
        print(-1)
        exit()

print(max(map(max, visited)) - 1)
    
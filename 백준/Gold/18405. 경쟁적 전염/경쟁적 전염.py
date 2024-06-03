import sys
from  collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

S, X, Y = map(int, input().split())

virus_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus_list.append((graph[i][j], 0, i, j))

virus_list.sort(key=lambda x: x[0])
q = deque(virus_list)

while q:
    virus, t, x, y = q.popleft()
    if t == S:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<n and 0<=ny<n):
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]
            q.append((graph[nx][ny], t+1, nx, ny))

if graph[X-1][Y-1] == 0:
    print(0)
elif graph[X-1][Y-1] >= 1:
    print(graph[X-1][Y-1])
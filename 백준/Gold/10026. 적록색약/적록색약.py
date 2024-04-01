import sys
import copy
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
visited = []
for i in range(n):
    graph.append(list(input().rstrip()))

graph_2 = copy.deepcopy(graph)

for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph_2[i][j] = "G"

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]

def bfs(i, j, a, graph):
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<n and 0<=ny<n):
                continue
            if graph[nx][ny] == a:
                graph[nx][ny] = 0
                q.append((nx, ny))

r = 0
g_1 = 0
g_2 = 0
b = 0 
for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            r += 1
            bfs(i, j, "R", graph)
        if graph[i][j] == "G":
            g_1 += 1
            bfs(i, j, "G", graph)
        if graph_2[i][j] == "G":
            g_2 += 1
            bfs(i, j, "G", graph_2)
        if graph[i][j] == "B":
            b += 1
            bfs(i, j, "B", graph)

print(r+g_1+b, g_2+b)
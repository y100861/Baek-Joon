import sys
import copy
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = copy.deepcopy(graph)

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = -2

    while q:
        x, y = q.popleft()

        if graph[x][y] == -1:
            return "HaruHaru"
        
        dx = [0, graph[x][y], 0, 0]
        dy = [0, 0, 0, graph[x][y]]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<n):
                continue
            
            if visited[nx][ny] != -2:
                visited[nx][ny] = -2
                q.append((nx, ny))

    return "Hing"

print(bfs(0, 0))
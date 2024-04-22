import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

blank = []
virus = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))
        if graph[i][j] == 0:
            blank.append((i, j))

result = 0
def bfs():
    
    for k in combinations(blank, 3):
        q = deque()
        visited = deepcopy(graph)

        for i in range(len(virus)):
            q.append(virus[i])

        for x, y in k:
            visited[x][y] = 1

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0<=nx<n and 0<=ny<m):
                    continue

                if visited[nx][ny] == 0:
                    visited[nx][ny] = 2
                    q.append((nx, ny))
        
        cnt = 0
        global result

        for row in range(n):
            cnt += visited[row].count(0)

        result = max(result, cnt)

bfs()
print(result)
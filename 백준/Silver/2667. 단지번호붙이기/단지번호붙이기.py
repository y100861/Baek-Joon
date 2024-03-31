import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    house = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<n and 0<=ny<n):
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                house += 1
                q.append((nx, ny))

    return house

cnt = 0

house_lst = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
            house_lst.append(bfs(i, j))

print(cnt)

house_lst.sort()
for num in house_lst:
    print(num)